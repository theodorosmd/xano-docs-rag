from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
import os

load_dotenv()

# Dossiers à scanner
folders = ["docs", "documentation", "bubble_docs", "xano_docs", "weweb-docs"]
all_docs = []

for folder in folders:
    if os.path.exists(folder):
        loader = DirectoryLoader(folder, glob="**/*.md", show_progress=True)
        all_docs.extend(loader.load())

# Séparation en chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
split_docs = splitter.split_documents(all_docs)

# Embedding & persist
embedding = OpenAIEmbeddings()
db = Chroma.from_documents(split_docs, embedding, persist_directory="./chroma_db")

db.persist()
print("✅ Ingestion complete")
