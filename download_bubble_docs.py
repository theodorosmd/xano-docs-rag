import requests
from bs4 import BeautifulSoup
import os
import time

def download_bubble_docs():
    """Download Bubble documentation from their official site."""
    base_url = "https://manual.bubble.io"
    visited_urls = set()
    docs_dir = "bubble_docs"
    
    # Create directory for Bubble docs if it doesn't exist
    if not os.path.exists(docs_dir):
        os.makedirs(docs_dir)
    
    def download_page(url):
        if url in visited_urls:
            return
        
        visited_urls.add(url)
        print(f"Downloading: {url}")
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract the main content
            main_content = soup.find('div', {'class': 'article-content'})
            if main_content:
                # Get the title
                title = soup.find('h1')
                title_text = title.text if title else "Untitled"
                
                # Create filename from URL
                filename = url.split('/')[-1]
                if not filename.endswith('.html'):
                    filename = f"{filename}.md"
                
                # Save the content
                with open(os.path.join(docs_dir, filename), 'w', encoding='utf-8') as f:
                    f.write(f"# {title_text}\n\n")
                    f.write(main_content.get_text(separator='\n\n'))
                
                print(f"Saved: {filename}")
                
                # Find and follow links
                for link in main_content.find_all('a'):
                    href = link.get('href')
                    if href and href.startswith('/'):
                        next_url = f"{base_url}{href}"
                        time.sleep(1)  # Be nice to the server
                        download_page(next_url)
        
        except Exception as e:
            print(f"Error downloading {url}: {str(e)}")
    
    # Start with the main documentation page
    download_page(f"{base_url}/")
    print("Bubble documentation download completed!")

if __name__ == "__main__":
    download_bubble_docs() 