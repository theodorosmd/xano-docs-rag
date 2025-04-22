from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

load_dotenv()

# Load the markdown file
loader = TextLoader("xano_docs.md")
docs = loader.load()

# Split into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
split_docs = splitter.split_documents(docs)

# Embed and store in Chroma
embedding = OpenAIEmbeddings()
db = Chroma.from_documents(split_docs, embedding, persist_directory="./chroma_db")

db.persist()
print("✅ Ingestion complete")
