from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

# Chargement de la DB
query = "What is Xano?"
embedding = OpenAIEmbeddings()
db = Chroma(persist_directory="./chroma_db", embedding_function=embedding)

retriever = db.as_retriever()
# Use invoke instead of get_relevant_documents
results = retriever.invoke(query)

print(f"🧠 Query: {query}")
print(f"📄 Found {len(results)} document(s):\n")

for doc in results:
    print("--- Document ---")
    print(doc.page_content)
