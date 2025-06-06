from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Créer l'app FastAPI
app = FastAPI()

# Schéma de requête
class Question(BaseModel):
    query: str

def init_db():
    """Initialize the Chroma database with documentation if it's empty."""
    # Initialize embeddings
    embeddings = OpenAIEmbeddings()
    
    # Create or load Chroma database
    db = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
    
    # Check if database is empty
    if len(db.get()['ids']) == 0:
        print("Initializing database with documentation...")
        
        # Load Xano documentation
        xano_loader = TextLoader("xano_docs.md")
        xano_docs = xano_loader.load()
        
        # Load Weweb documentation
        weweb_docs = []
        for file in os.listdir():
            if file.endswith('.md'):
                loader = TextLoader(file)
                weweb_docs.extend(loader.load())
        
        # Load Bubble documentation
        bubble_docs = []
        bubble_dir = "bubble_docs"
        if os.path.exists(bubble_dir):
            for file in os.listdir(bubble_dir):
                if file.endswith('.md'):
                    loader = TextLoader(os.path.join(bubble_dir, file))
                    bubble_docs.extend(loader.load())
        
        # Combine all documents
        all_docs = xano_docs + weweb_docs + bubble_docs
        
        # Split documents into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        chunks = text_splitter.split_documents(all_docs)
        
        # Add documents to the database
        db.add_documents(chunks)
        print(f"Added {len(chunks)} document chunks to the database")
    else:
        print("Database already contains data.")

# Initialize database on startup
init_db()

# Endpoint pour traiter une question
@app.post("/ask")
async def ask_question(data: Question):
    try:
        # Initialize embeddings and database
        embeddings = OpenAIEmbeddings()
        db = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
        
        # Create QA chain
        qa = RetrievalQA.from_chain_type(
            llm=ChatOpenAI(model_name="gpt-4"),
            chain_type="stuff",
            retriever=db.as_retriever()
        )
        
        # Get answer
        result = qa.invoke({"query": data.query})
        
        return {"answer": result["result"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
