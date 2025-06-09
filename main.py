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
from middleware import RateLimitMiddleware, verify_api_key

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('api.log'),
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

@app.get("/health")
async def health_check():
    try:
        embeddings = OpenAIEmbeddings()
        db = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
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
        db = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
        retriever = db.as_retriever()
        llm = ChatOpenAI(
            model_name="gpt-4",
            temperature=0,
            max_tokens=1024,
            top_p=1
        )

        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are an expert answering questions about a technical documentation."),
            ("human", "Context:\n{context}\n\nQuestion: {input}")
        ])

        document_chain = create_stuff_documents_chain(llm, prompt)
        qa = create_retrieval_chain(retriever, document_chain)

        result = qa.invoke({"input": data.query})
        answer = result["answer"]
        duration = time.time() - start_time

        logger.info(f"Answer: {answer[:200]}... in {duration:.2f}s")
        return SuccessResponse(
            response=answer,
            processing_time=duration,
            timestamp=datetime.utcnow().isoformat()
        )

    except Exception as e:
        logger.error(f"Error while processing question: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail="An error occurred while processing your question.")
