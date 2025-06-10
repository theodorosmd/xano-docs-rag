from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os
import logging
from typing import Optional
import time
from datetime import datetime
# Assurez-vous que l'import de verify_api_key est correct
from middleware import RateLimitMiddleware, verify_api_key

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        # Gardez le FileHandler pour le développement local si vous le souhaitez, mais il peut ne pas persister sur Render
        # logging.FileHandler('api.log'), 
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

load_dotenv()

app = FastAPI(
    title="Documentation RAG API",
    description="API for querying documentation using RAG",
    version="1.0.0"
)

app.add_middleware(RateLimitMiddleware)

# --- Schémas de données (Pydantic Models) ---
class Question(BaseModel):
    query: str = Field(..., min_length=1, max_length=1000)

class ErrorResponse(BaseModel):
    error: str
    detail: Optional[str] = None
    timestamp: str

class SuccessResponse(BaseModel):
    response: str
    processing_time: float
    timestamp: str

# --- Middlewares et Handlers ---
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    logger.info(f"{request.method} {request.url.path} - {response.status_code} in {duration:.2f}s")
    return response

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled error: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content=ErrorResponse(
            error="Internal Server Error",
            detail=str(exc),
            timestamp=datetime.utcnow().isoformat()
        ).dict()
    )

# --- Endpoints de l'API ---

# NOUVEL ENDPOINT DE TEST
@app.get("/version")
async def get_version():
    """
    Retourne une version statique pour vérifier si le dernier déploiement est en ligne.
    """
    return {"version": "1.1", "description": "API avec le middleware de sécurité corrigé."}


@app.get("/health")
async def health_check():
    try:
        embeddings = OpenAIEmbeddings()
        # Le chemin de la base de données doit être adapté à l'environnement de Render
        db = Chroma(persist_directory="/opt/render/project/src/chroma_db", embedding_function=embeddings)
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        raise HTTPException(status_code=503, detail="Service unhealthy")

@app.post("/ask", response_model=SuccessResponse, dependencies=[Depends(verify_api_key)])
async def ask_question(data: Question):
    start_time = time.time()
    try:
        logger.info(f"Received question: {data.query[:80]}...")

        embeddings = OpenAIEmbeddings()
        db = Chroma(persist_directory="/opt/render/project/src/chroma_db", embedding_function=embeddings)
        retriever = db.as_retriever()
        llm = ChatOpenAI(
            model_name="gpt-4", # Fixed model name
            temperature=0,
            max_tokens=1024
        )

        prompt = ChatPromptTemplate.from_template(
            "Answer the following question based only on the provided context.\n\n"
            "Context: {context}\n\n"
            "Question: {input}\n\n"
            "Answer:"
        )

        document_chain = create_stuff_documents_chain(llm, prompt)
        qa = create_retrieval_chain(retriever, document_chain)

        result = qa.invoke({"input": data.query})
        answer = result.get("answer", "No answer found in the context.")
        duration = time.time() - start_time

        logger.info(f"Answer generated in {duration:.2f}s")
        return SuccessResponse(
            response=answer,
            processing_time=duration,
            timestamp=datetime.utcnow().isoformat()
        )

    except Exception as e:
        logger.error(f"Error while processing question: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail="An error occurred while processing your question.")
