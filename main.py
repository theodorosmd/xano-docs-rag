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

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(
    title="Documentation RAG API",
    description="API for querying documentation using RAG",
    version="1.0.0"
)

# Add middleware
app.add_middleware(RateLimitMiddleware)

# Request schema with validation
class Question(BaseModel):
    query: str = Field(..., min_length=1, max_length=1000, description="The question to ask about the documentation")

# Response schemas
class ErrorResponse(BaseModel):
    error: str
    detail: Optional[str] = None
    timestamp: str

class SuccessResponse(BaseModel):
    response: str
    processing_time: float
    timestamp: str

# Middleware for request logging
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    logger.info(f"Request: {request.method} {request.url.path} - Status: {response.status_code} - Time: {process_time:.2f}s")
    return response

# Error handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Global error handler caught: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content=ErrorResponse(
            error="Internal Server Error",
            detail=str(exc),
            timestamp=datetime.utcnow().isoformat()
        ).dict()
    )

# Health check endpoint
@app.get("/health")
async def health_check():
    try:
        # Test database connection
        embeddings = OpenAIEmbeddings()
        db = Chroma(persist_directory="/opt/render/chroma_db", embedding_function=embeddings)
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        raise HTTPException(status_code=503, detail="Service unhealthy")

# Question endpoint
@app.post("/ask", response_model=SuccessResponse, dependencies=[Depends(verify_api_key)])
async def ask_question(data: Question):
    start_time = time.time()
    try:
        logger.info(f"Processing question: {data.query[:100]}...")
        
        embeddings = OpenAIEmbeddings()
        db = Chroma(persist_directory="/opt/render/chroma_db", embedding_function=embeddings)
        retriever = db.as_retriever()
        llm = ChatOpenAI(
            model_name="gpt-4",
            temperature=0,
            max_tokens=1024,
            top_p=1,
            streaming=True
        )
        
        # Create the prompt template
        prompt = ChatPromptTemplate.from_template("""Answer the following question based on the provided context:
        
        Context: {context}
        
        Question: {input}
        
        Answer:""")
        
        # Create the document chain
        document_chain = create_stuff_documents_chain(llm, prompt)
        
        # Create the retrieval chain
        qa = create_retrieval_chain(retriever, document_chain)
        
        result = qa.invoke({"input": data.query})
        logger.info(f"Result from QA invoke: {result}")
        processing_time = time.time() - start_time
        
        logger.info(f"Question processed successfully in {processing_time:.2f}s")
        
        return SuccessResponse(
            response=result["answer"],
            processing_time=processing_time,
            timestamp=datetime.utcnow().isoformat()
        )
    except Exception as e:
        logger.error(f"Error processing question: {str(e)} - Type: {type(e).__name__} - Args: {e.args}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Error processing question: {str(e)} - Please check logs for more details."
        )
