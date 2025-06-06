from fastapi import FastAPI
from pydantic import BaseModel
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import os

# Charger les variables d'environnement
load_dotenv()

# Créer l'app FastAPI
app = FastAPI()

# Schéma de requête
class Question(BaseModel):
    query: str

# Endpoint pour traiter une question
@app.post("/ask")
async def ask_question(data: Question):
    embeddings = OpenAIEmbeddings()
    db = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
    retriever = db.as_retriever()
    llm = ChatOpenAI(model_name="gpt-4",
    temperature=0,
    max_tokens=1024,
    top_p=1,
    streaming=True)
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    
    result = qa.invoke({"query": data.query})
    return {"response": result["result"]}
