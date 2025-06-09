import pytest
from fastapi.testclient import TestClient
from main import app
import os
from unittest.mock import patch, MagicMock

client = TestClient(app)

# Mock environment variables
@pytest.fixture(autouse=True)
def mock_env_vars():
    with patch.dict(os.environ, {
        "OPENAI_API_KEY": "test_key",
        "API_KEY": "test_api_key"
    }):
        yield

# Test health check endpoint
def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

# Test ask endpoint without API key
def test_ask_without_api_key():
    response = client.post("/ask", json={"query": "test question"})
    assert response.status_code == 401
    assert "API key is missing" in response.json()["detail"]

# Test ask endpoint with invalid API key
def test_ask_with_invalid_api_key():
    response = client.post(
        "/ask",
        json={"query": "test question"},
        headers={"X-API-Key": "invalid_key"}
    )
    assert response.status_code == 401
    assert "Invalid API key" in response.json()["detail"]

# Test ask endpoint with valid API key
@patch("main.OpenAIEmbeddings")
@patch("main.ChatOpenAI")
@patch("main.Chroma")
def test_ask_with_valid_api_key(mock_chroma, mock_chat, mock_embeddings):
    # Mock the response from the QA chain
    mock_result = {"answer": "Test answer"}
    
    # Setup mocks
    mock_embeddings.return_value = MagicMock()
    mock_chroma.return_value = MagicMock()
    mock_chat.return_value = MagicMock()
    
    # Mock the QA chain
    mock_qa = MagicMock()
    mock_qa.invoke.return_value = mock_result
    
    with patch("main.create_retrieval_chain", return_value=mock_qa):
        response = client.post(
            "/ask",
            json={"query": "test question"},
            headers={"X-API-Key": "test_api_key"}
        )
        
        assert response.status_code == 200
        assert response.json()["response"] == "Test answer"
        assert "processing_time" in response.json()
        assert "timestamp" in response.json()

# Test rate limiting
def test_rate_limiting():
    # Make multiple requests in quick succession
    for _ in range(61):  # One more than the limit
        response = client.post(
            "/ask",
            json={"query": "test question"},
            headers={"X-API-Key": "test_api_key"}
        )
    
    # The last request should be rate limited
    assert response.status_code == 429
    assert "Too many requests" in response.json()["detail"]

# Test input validation
def test_input_validation():
    # Test empty query
    response = client.post(
        "/ask",
        json={"query": ""},
        headers={"X-API-Key": "test_api_key"}
    )
    assert response.status_code == 422
    
    # Test query too long
    response = client.post(
        "/ask",
        json={"query": "a" * 1001},
        headers={"X-API-Key": "test_api_key"}
    )
    assert response.status_code == 422

# Test error handling
@patch("main.OpenAIEmbeddings")
def test_error_handling(mock_embeddings):
    # Mock an error
    mock_embeddings.side_effect = Exception("Test error")
    
    response = client.post(
        "/ask",
        json={"query": "test question"},
        headers={"X-API-Key": "test_api_key"}
    )
    
    assert response.status_code == 500
    assert "Error processing question" in response.json()["detail"]
    assert "timestamp" in response.json() 