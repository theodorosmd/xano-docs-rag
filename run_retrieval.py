import os
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

# Load environment variables (for OpenAI API key)
load_dotenv()

print("--- Processing documents and building Chroma DB ---")
loader = DirectoryLoader("docs", glob="**/*.md", show_progress=True)
docs = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)

# Ensure chroma_db directory exists before creating Chroma instance if it was just removed
if not os.path.exists("chroma_db"):
    os.makedirs("chroma_db")

db = Chroma.from_documents(
    documents=splits,
    embedding=OpenAIEmbeddings(),
    persist_directory="chroma_db"
)
# db.persist()  # Removed as it's not available in the new Chroma version
print("--- Chroma DB built and persisted ---")

print("\n--- Retrieving documents for query: 'What is Xano?' ---")
retriever = db.as_retriever()
results = retriever.get_relevant_documents("What is Xano?")
for doc in results:
    print("---")
    print(doc.page_content)

print("--- Retrieval query complete ---") 