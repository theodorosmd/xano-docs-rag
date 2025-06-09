from fastapi import Request, HTTPException
from fastapi.security import APIKeyHeader
from starlette.middleware.base import BaseHTTPMiddleware
import time
from typing import Dict, Tuple
import os
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)

# Rate limiting configuration
RATE_LIMIT_WINDOW = 60  # 1 minute
MAX_REQUESTS_PER_WINDOW = 60  # 60 requests per minute

# Store for rate limiting
request_history: Dict[str, list] = {}

class RateLimitMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        
        # Clean old requests
        current_time = time.time()
        if client_ip in request_history:
            request_history[client_ip] = [
                req_time for req_time in request_history[client_ip]
                if current_time - req_time < RATE_LIMIT_WINDOW
            ]
        
        # Check rate limit
        if client_ip in request_history and len(request_history[client_ip]) >= MAX_REQUESTS_PER_WINDOW:
            logger.warning(f"Rate limit exceeded for IP: {client_ip}")
            raise HTTPException(
                status_code=429,
                detail="Too many requests. Please try again later."
            )
        
        # Add current request
        if client_ip not in request_history:
            request_history[client_ip] = []
        request_history[client_ip].append(current_time)
        
        return await call_next(request)

# API Key authentication
API_KEY_NAME = "X-API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME)

async def verify_api_key(api_key: str = api_key_header):
    if not api_key:
        raise HTTPException(
            status_code=401,
            detail="API key is missing"
        )
    
    # Get API key from environment variable
    valid_api_key = os.getenv("API_KEY")
    if not valid_api_key:
        logger.warning("API_KEY environment variable not set")
        raise HTTPException(
            status_code=500,
            detail="API key validation not configured"
        )
    
    if api_key != valid_api_key:
        logger.warning(f"Invalid API key attempt: {api_key[:5]}...")
        raise HTTPException(
            status_code=401,
            detail="Invalid API key"
        )
    
    return api_key 