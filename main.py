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
from typing import Optional, List, Dict, Any
import time
from datetime import datetime
from middleware import RateLimitMiddleware, verify_api_key

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
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

class DebugDocument(BaseModel):
    content: str
    metadata: Dict[str, Any]

class DebugResponse(BaseModel):
    query: str
    retrieved_documents_count: int
    retrieved_documents: List[DebugDocument]


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

@app.get("/version")
async def get_version():
    return {"version": "1.2", "description": "API with retriever debugging endpoint."}


@app.get("/health")
async def health_check():
    try:
        embeddings = OpenAIEmbeddings()
        db = Chroma(persist_directory="/opt/render/project/src/chroma_db", embedding_function=embeddings)
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        raise HTTPException(status_code=503, detail="Service unhealthy")


# NOUVEL ENDPOINT DE DÉBOGAGE
@app.post("/debug-retriever", response_model=DebugResponse, dependencies=[Depends(verify_api_key)])
async def debug_retriever(data: Question):
    """
    Cet endpoint teste uniquement la partie "Retrieval".
    Il retourne les documents trouvés dans ChromaDB pour une question donnée, sans appeler l'IA.
    """
    try:
        logger.info(f"DEBUG: Testing retriever for question: {data.query}")
        
        embeddings = OpenAIEmbeddings()
        db = Chroma(
            persist_directory="/opt/render/project/src/chroma_db", 
            embedding_function=embeddings
        )
        retriever = db.as_retriever()
        
        # Étape clé : on récupère les documents sans appeler le LLM
        retrieved_docs = retriever.invoke(data.query)
        
        logger.info(f"DEBUG: Found {len(retrieved_docs)} documents.")
        
        # On retourne le contenu des documents trouvés
        return DebugResponse(
            query=data.query,
            retrieved_documents_count=len(retrieved_docs),
            retrieved_documents=[
                DebugDocument(content=doc.page_content, metadata=doc.metadata) 
                for doc in retrieved_docs
            ]
        )
    except Exception as e:
        logger.error(f"DEBUG: Error in retriever test: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/ask", response_model=SuccessResponse, dependencies=[Depends(verify_api_key)])
async def ask_question(data: Question):
    start_time = time.time()
    try:
        logger.info(f"Received question: {data.query[:80]}...")

        embeddings = OpenAIEmbeddings()
        db = Chroma(persist_directory="/opt/render/project/src/chroma_db", embedding_function=embeddings)
        retriever = db.as_retriever()
        llm = ChatOpenAI(
            model_name="gpt-4o",
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