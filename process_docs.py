from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import re
from tqdm import tqdm
import warnings
from bs4 import XMLParsedAsHTMLWarning
import json

# Ignore XML parsing warnings
warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

# Load environment variables
load_dotenv()

PROGRESS_FILE = "processing_progress.json"

def load_progress():
    """Load the processing progress from file."""
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, 'r') as f:
            data = json.load(f)
            # Convert list back to set
            data["processed_files"] = set(data["processed_files"])
            return data
    return {"processed_files": set(), "last_batch": 0}

def save_progress(progress):
    """Save the processing progress to file."""
    # Convert set to list for JSON serialization
    progress_copy = progress.copy()
    progress_copy["processed_files"] = list(progress["processed_files"])
    with open(PROGRESS_FILE, 'w') as f:
        json.dump(progress_copy, f)

def clean_text(text):
    """Clean text by removing special tokens and normalizing whitespace."""
    # Remove special tokens
    text = re.sub(r'<\|.*?\|>', '', text)
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Remove HTML entities
    text = re.sub(r'&[a-zA-Z]+;', '', text)
    
    return text.strip()

def process_html_file(file_path):
    """Process an HTML file and extract its text content."""
    with open(file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Parse HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Remove script and style elements
    for script in soup(["script", "style"]):
        script.decompose()
    
    # Get text
    text = soup.get_text()
    
    # Clean the text
    text = clean_text(text)
    
    return text

def process_documentation():
    """Process all documentation files and create embeddings."""
    # Load progress
    progress = load_progress()
    processed_files = progress["processed_files"]
    last_batch = progress["last_batch"]
    
    print(f"Resuming from batch {last_batch}")
    
    # Initialize the text splitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,  # Smaller chunks
        chunk_overlap=50,  # Smaller overlap
        length_function=len,
    )
    
    # Initialize the embedding model
    embeddings = OpenAIEmbeddings()
    
    # Process each documentation directory
    docs_dir = "documentation"
    all_docs = []
    
    # First, collect all documents
    for source_dir in os.listdir(docs_dir):
        source_path = os.path.join(docs_dir, source_dir)
        if os.path.isdir(source_path):
            print(f"Processing {source_dir}...")
            
            for file in os.listdir(source_path):
                if file.endswith('.html'):
                    file_path = os.path.join(source_path, file)
                    
                    # Skip already processed files
                    if file_path in processed_files:
                        print(f"Skipping already processed file: {file}")
                        continue
                    
                    try:
                        # Process the HTML file
                        text = process_html_file(file_path)
                        
                        # Skip empty or very short texts
                        if len(text) < 50:
                            continue
                        
                        # Split the text into smaller chunks
                        chunks = text_splitter.split_text(text)
                        
                        # Create documents for each chunk
                        for i, chunk in enumerate(chunks):
                            doc = {
                                'content': chunk,
                                'metadata': {
                                    'source': source_dir,
                                    'file': file,
                                    'chunk': i
                                }
                            }
                            all_docs.append(doc)
                        
                        # Mark file as processed
                        processed_files.add(file_path)
                        save_progress({"processed_files": processed_files, "last_batch": last_batch})
                        
                    except Exception as e:
                        print(f"Error processing {file}: {str(e)}")
    
    # Process documents in smaller batches
    batch_size = 20  # Process 20 documents at a time
    total_batches = (len(all_docs) + batch_size - 1) // batch_size
    
    print(f"Processing {len(all_docs)} documents in {total_batches} batches...")
    
    # Initialize the database
    db = None
    
    # Skip to the last processed batch
    start_idx = last_batch * batch_size
    
    for i in tqdm(range(start_idx, len(all_docs), batch_size)):
        batch = all_docs[i:i + batch_size]
        
        # Split documents into chunks
        texts = [doc['content'] for doc in batch]
        metadatas = [doc['metadata'] for doc in batch]
        
        try:
            # Create or update the vector store
            if db is None:
                # First batch - create new store
                db = Chroma.from_texts(
                    texts=texts,
                    embedding=embeddings,
                    metadatas=metadatas,
                    persist_directory="./chroma_db"
                )
            else:
                # Subsequent batches - add to existing store
                db.add_texts(
                    texts=texts,
                    metadatas=metadatas
                )
            
            # Persist after each batch
            db.persist()
            
            # Update progress
            current_batch = (i + batch_size) // batch_size
            save_progress({"processed_files": processed_files, "last_batch": current_batch})
            
        except Exception as e:
            print(f"Error processing batch {i//batch_size + 1}: {str(e)}")
            continue
    
    print("✅ Processing complete")

if __name__ == "__main__":
    process_documentation() 