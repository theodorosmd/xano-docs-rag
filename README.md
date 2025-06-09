# Documentation RAG API

A Retrieval-Augmented Generation (RAG) API for querying documentation from various sources including Xano, WeWeb, and more.

## Features

- Document processing and embedding generation
- Vector database storage using Chroma
- FastAPI-based REST API
- Support for multiple documentation sources
- Progress tracking and resumable processing

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd xano-docs-rag
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory with:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

### Processing Documentation

1. Download documentation:
```bash
python download_all_docs.py
```

2. Process and embed documents:
```bash
python process_docs.py
```

### Running the API

Start the server:
```bash
uvicorn main:app --reload --port 3000
```

The API will be available at `http://127.0.0.1:3000`

## API Endpoints

### Health Check
```
GET /health
```
Returns the API health status.

### Ask Question
```
POST /ask
```
Query the documentation with a question.

Request body:
```json
{
    "query": "Your question here"
}
```

Response:
```json
{
    "response": "Answer based on the documentation"
}
```

## Project Structure

- `main.py`: FastAPI application and endpoints
- `process_docs.py`: Document processing and embedding generation
- `download_all_docs.py`: Documentation downloader
- `chroma_db/`: Vector database storage
- `documentation/`: Downloaded documentation files

## Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key
- `PORT`: API server port (default: 3000)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License
