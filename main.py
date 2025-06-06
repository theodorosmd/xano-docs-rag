from fastapi import FastAPI
from pydantic import BaseModel
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv
import os

# Charger les variables d'environnement
load_dotenv()

# Créer l'app FastAPI
app = FastAPI()

# Initialize database
def init_db():
    embeddings = OpenAIEmbeddings()
    db = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
    
    # Check if database is empty
    if db._collection.count() == 0:
        print("Initializing database with Xano documentation...")
        # Load the documentation
        loader = TextLoader("xano_docs.md")
        documents = loader.load()
        
        # Split the text
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
        )
        texts = text_splitter.split_documents(documents)
        
        # Add to database
        db.add_documents(texts)
        db.persist()
        print("Database initialized!")
    else:
        print("Database already contains data.")
    
    return db

# Initialize database on startup
db = init_db()

# Schéma de requête
class Question(BaseModel):
    query: str

# Endpoint pour traiter une question
@app.post("/ask")
async def ask_question(data: Question):
    embeddings = OpenAIEmbeddings()
    retriever = db.as_retriever()
    llm = ChatOpenAI(model_name="gpt-4",
    temperature=0,
    max_tokens=1024,
    top_p=1,
    streaming=True)
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    
    result = qa.invoke({"query": data.query})
    return {"response": result["result"]}
