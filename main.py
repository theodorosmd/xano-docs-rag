# Fichier : main.py (Version avec Streaming SSE)

from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.responses import JSONResponse, StreamingResponse
from pydantic import BaseModel, Field
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os
import logging
from typing import Optional, List, Dict, Any, AsyncGenerator
import time
import json
import asyncio
from datetime import datetime
from middleware import RateLimitMiddleware, verify_api_key

# --- Configuration ---
DB_PERSIST_PATH = "/data/chroma_db"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

load_dotenv()

app = FastAPI(
    title="Documentation RAG API",
    description="API for querying documentation using RAG with Streaming",
    version="1.1.0"
)

app.add_middleware(RateLimitMiddleware)

# --- Schémas de données ---
class Question(BaseModel):
    query: str = Field(..., min_length=1, max_length=1000)

# --- Middlewares et Handlers ---
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    logger.info(f"{request.method} {request.url.path} - {response.status_code} in {duration:.2f}s")
    return response

# ... (Les autres endpoints comme /health, /version, etc. peuvent rester les mêmes)

# --- Endpoint /ask avec Streaming ---

async def stream_rag_response(data: Question) -> AsyncGenerator[str, None]:
    """
    Cette fonction est un générateur asynchrone qui streame la réponse du RAG.
    """
    try:
        logger.info(f"Streaming request received for: {data.query[:80]}...")

        embeddings = OpenAIEmbeddings()
        db = Chroma(persist_directory=DB_PERSIST_PATH, embedding_function=embeddings)
        retriever = db.as_retriever()
        
        # S'assurer que le LLM est configuré pour le streaming
        llm = ChatOpenAI(
            model_name="gpt-4o",
            temperature=0,
            max_tokens=1024,
            streaming=True # Important pour LangChain
        )

        prompt = ChatPromptTemplate.from_template(
            "Answer the following question based only on the provided context.\n\n"
            "Context: {context}\n\n"
            "Question: {input}\n\n"
            "Answer:"
        )

        document_chain = create_stuff_documents_chain(llm, prompt)
        qa = create_retrieval_chain(retriever, document_chain)

        # Utiliser .stream() au lieu de .invoke()
        async for chunk in qa.astream({"input": data.query}):
            # La réponse de l'IA se trouve dans la clé 'answer'
            if "answer" in chunk:
                answer_piece = chunk["answer"]
                if answer_piece:
                    # Formater le chunk en tant qu'événement Server-Sent Event (SSE)
                    # C'est le format que votre script JS sur WeWeb attend.
                    # Il est compatible avec ce que Xano peut relayer.
                    sse_chunk = {"var": {"response_text": answer_piece}}
                    yield f"data: {json.dumps(sse_chunk)}\n\n"
                    # Petite pause pour permettre au réseau de "respirer"
                    await asyncio.sleep(0.01)

    except Exception as e:
        logger.error(f"Error during streaming: {str(e)}", exc_info=True)
        error_message = {"error": "An error occurred during streaming."}
        yield f"data: {json.dumps(error_message)}\n\n"

@app.post("/ask", dependencies=[Depends(verify_api_key)])
async def ask_question_streaming(data: Question):
    """
    Endpoint principal qui renvoie la réponse de l'IA en streaming (SSE).
    """
    return StreamingResponse(
        stream_rag_response(data), 
        media_type="text/event-stream"
    )
