import os
import asyncio
import aiohttp
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time
from typing import Set, Dict, List
import logging
import json
from datetime import datetime, timedelta
import tqdm.asyncio
import xml.etree.ElementTree as ET

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DocumentationDownloader:
    def __init__(self, base_output_dir: str = "documentation"):
        self.base_output_dir = base_output_dir
        self.visited_urls: Set[str] = set()
        self.session = None
        self.semaphore = asyncio.Semaphore(10)  # Increased from 5 to 10 concurrent downloads
        self.progress_file = os.path.join(base_output_dir, "download_progress.json")
        self.start_time = None
        self.total_pages = 0
        self.downloaded_pages = 0
        self.source_progress = {}
        self.max_depth = 5  # Maximum depth for crawling
        self.current_depth = 0
        self.failed_urls = set()  # Track failed URLs

    async def init_session(self):
        if not self.session:
            self.session = aiohttp.ClientSession()

    async def close_session(self):
        if self.session:
            await self.session.close()
            self.session = None

    def create_output_dir(self, source_name: str) -> str:
        output_dir = os.path.join(self.base_output_dir, source_name)
        os.makedirs(output_dir, exist_ok=True)
        return output_dir

    def clean_filename(self, url: str) -> str:
        parsed = urlparse(url)
        path = parsed.path.strip('/')
        if not path:
            return 'index.html'
        return path.replace('/', '_') + '.html'

    def load_progress(self):
        if os.path.exists(self.progress_file):
            with open(self.progress_file, 'r') as f:
                data = json.load(f)
                self.visited_urls = set(data.get('visited_urls', []))
                self.source_progress = data.get('source_progress', {})
                return True
        return False

    def save_progress(self):
        os.makedirs(os.path.dirname(self.progress_file), exist_ok=True)
        with open(self.progress_file, 'w') as f:
            json.dump({
                'visited_urls': list(self.visited_urls),
                'source_progress': self.source_progress,
                'timestamp': datetime.now().isoformat()
            }, f)

    async def download_page(self, url: str, output_dir: str, source_name: str, depth: int = 0) -> List[str]:
        if depth > self.max_depth:
            logger.warning(f"Max depth reached for {url}")
            return []
            
        # Normalize URL for visited check
        parsed_url = urlparse(url)
        normalized_url = parsed_url._replace(query="", fragment="").geturl().rstrip('/')
        if normalized_url in self.visited_urls:
            return []
        self.visited_urls.add(normalized_url)
        filename = self.clean_filename(url)
        output_path = os.path.join(output_dir, filename)

        try:
            async with self.semaphore:
                logger.info(f"Downloading {url} (depth: {depth})")
                async with self.session.get(url) as response:
                    if response.status != 200:
                        logger.warning(f"Failed to download {url}: Status {response.status}")
                        self.failed_urls.add(url)
                        return []
                    
                    content = await response.text()
                    with open(output_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    self.downloaded_pages += 1
                    self.source_progress[source_name] = self.source_progress.get(source_name, 0) + 1
                    
                    # Save progress every 10 pages
                    if self.downloaded_pages % 10 == 0:
                        self.save_progress()
                    
                    # Calculate and display progress
                    elapsed_time = time.time() - self.start_time
                    pages_per_second = self.downloaded_pages / elapsed_time if elapsed_time > 0 else 0
                    remaining_pages = self.total_pages - self.downloaded_pages
                    estimated_seconds = remaining_pages / pages_per_second if pages_per_second > 0 else 0
                    
                    logger.info(f"Progress: {self.downloaded_pages}/{self.total_pages} pages "
                              f"({(self.downloaded_pages/self.total_pages*100):.1f}%) | "
                              f"ETA: {timedelta(seconds=int(estimated_seconds))} | "
                              f"Speed: {pages_per_second:.1f} pages/s")
                    
                    # Extract links for further downloading
                    soup = BeautifulSoup(content, 'html.parser')
                    links = []
                    for a in soup.find_all('a', href=True):
                        href = a['href']
                        full_url = urljoin(url, href)
                        if self.should_download_link(full_url, url):
                            links.append(full_url)
                    return links
        except Exception as e:
            logger.error(f"Error downloading {url}: {str(e)}")
            self.failed_urls.add(url)
            return []

    def should_download_link(self, link: str, base_url: str) -> bool:
        parsed_link = urlparse(link)
        parsed_base = urlparse(base_url)

        # Only follow links from the same domain (ignore www. prefix differences)
        def normalize_netloc(netloc):
            return netloc.lower().replace('www.', '')
        if normalize_netloc(parsed_link.netloc) != normalize_netloc(parsed_base.netloc):
            return False

        # Skip anchors and fragments
        if parsed_link.fragment:
            return False

        # Skip non-HTML resources
        non_html_exts = (
            '.jpg', '.jpeg', '.png', '.gif', '.svg', '.ico', '.pdf', '.zip', '.tar', '.gz', '.rar', '.7z',
            '.css', '.js', '.woff', '.woff2', '.ttf', '.eot', '.mp4', '.mp3', '.avi', '.mov', '.wmv', '.json', '.xml'
        )
        if any(parsed_link.path.lower().endswith(ext) for ext in non_html_exts):
            return False

        # Normalize URL (remove query for duplicate detection)
        normalized_url = parsed_link._replace(query="", fragment="").geturl().rstrip('/')
        if normalized_url in self.visited_urls:
            return False

        return True

    async def fetch_sitemap_urls(self, base_url: str) -> List[str]:
        """Try to fetch and parse sitemap.xml for a given base URL."""
        sitemap_urls = []
        # Try common sitemap locations
        candidates = [
            urljoin(base_url, '/sitemap.xml'),
            urljoin(base_url, 'sitemap.xml'),
            urljoin(base_url, '/docs/sitemap.xml'),
            urljoin(base_url, '/documentation/sitemap.xml'),
        ]
        for sitemap_url in candidates:
            try:
                async with self.session.get(sitemap_url) as response:
                    if response.status == 200:
                        text = await response.text()
                        try:
                            root = ET.fromstring(text)
                            for url in root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc'):
                                loc = url.text.strip()
                                if loc:
                                    sitemap_urls.append(loc)
                            if sitemap_urls:
                                logger.info(f"Found {len(sitemap_urls)} URLs in sitemap: {sitemap_url}")
                                return sitemap_urls
                        except Exception as e:
                            logger.warning(f"Failed to parse sitemap {sitemap_url}: {e}")
            except Exception as e:
                logger.warning(f"Failed to fetch sitemap {sitemap_url}: {e}")
        return []

    async def download_documentation(self, source_name: str, base_url: str):
        output_dir = self.create_output_dir(source_name)
        logger.info(f"\nStarting download for {source_name}...")

        # Try to fetch sitemap URLs first
        sitemap_urls = await self.fetch_sitemap_urls(base_url)
        urls_to_visit = [(url, 0) for url in sitemap_urls] if sitemap_urls else [(base_url, 0)]
        visited_this_source = set()
        while urls_to_visit:
            current_url, depth = urls_to_visit.pop(0)
            if current_url in visited_this_source:
                continue
            visited_this_source.add(current_url)
            new_links = await self.download_page(current_url, output_dir, source_name, depth)
            urls_to_visit.extend([(link, depth + 1) for link in new_links if link not in self.visited_urls])
            await asyncio.sleep(0.2)  # Reduced delay from 0.5 to 0.2 seconds

async def main():
    docs_sources = {
        'weweb': 'https://docs.weweb.io',
        'xano': 'https://docs.xano.com',
        'qdrant': 'https://qdrant.tech/documentation',
        'n8n': 'https://docs.n8n.io',
        'airtable': 'https://airtable.com/developers/web/api/introduction',
        'bubble': 'https://bubble.io/help',
        'llama': 'https://docs.llama-api.com',
        'coreweave': 'https://docs.coreweave.com',
        'llamaindex': 'https://docs.llamaindex.ai',
    }
    
    downloader = DocumentationDownloader()
    await downloader.init_session()
    
    try:
        # Load previous progress if exists
        if downloader.load_progress():
            logger.info("Resuming from previous download progress...")
            logger.info(f"Failed URLs from previous run: {len(downloader.failed_urls)}")
        
        downloader.start_time = time.time()
        downloader.total_pages = sum(downloader.source_progress.values()) + 1000  # Initial estimate
        
        # Create tasks for all documentation sources
        tasks = [
            downloader.download_documentation(source_name, url)
            for source_name, url in docs_sources.items()
        ]
        
        # Run all downloads concurrently
        await asyncio.gather(*tasks)
        
    finally:
        await downloader.close_session()
        downloader.save_progress()
        logger.info(f"Download completed. Failed URLs: {len(downloader.failed_urls)}")

if __name__ == "__main__":
    asyncio.run(main()) 