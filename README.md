# AI Knowledge Assistant - Mini RAG API

Artificial Intelligence API for document-based question answering using RAG (Retrieval-Augmented Generation).

## 🚀 Features

* Multi-format document processing and analysis (`.txt`, `.pdf`, `.docx`, `.md`, `.csv`, `.xlsx`, `.xls`)
* Embedding system using Sentence Transformers (via `HuggingFaceEmbeddings`)
* Semantic search with FAISS (LangChain vector store)
* Response generation using Groq LLM
* RESTful API built with FastAPI
* Retrieval with context expansion to improve answer coherence and accuracy

## 📋 Requirements

* Python 3.12+
* pip

> The **Groq API key** (`GROQ_API_KEY`) can be obtained for free by creating an account on the Groq Console:
> [Groq Console](https://console.groq.com/keys?utm_source=chatgpt.com)

## 🛠️ Local Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd "AI Knowledge Assistant (Mini-RAG API)"
```

2. Create and activate the virtual environment:

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Configure environment variables:

```bash
cp .env.example .env
# Edit the .env file with your values
```

5. Start the server:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at:

```bash
http://localhost:8000
```

## 🔑 Required Environment Variables

| Variable          | Description                                         | Required                    |
| ----------------- | --------------------------------------------------- | --------------------------- |
| `ENV`             | Runtime environment (`development` or `production`) | No (default: `development`) |
| `GROQ_API_KEY`    | Groq API key for the LLM                            | Yes                         |
| `FRONTEND_URL`    | Frontend URL in production                          | Yes (production only)       |
| `ALLOWED_ORIGINS` | Allowed CORS origins (comma-separated)              | No                          |

## 📚 Main Endpoints

### Health Check

```http
GET /api/health
```

### Upload Document

```http
POST /api/upload
Content-Type: multipart/form-data

Body:
file (document to process)
```

### Ask a Question

```http
POST /api/ask
Content-Type: application/json

Body:
{
  "question": "your question here",
  "k": 5
}
```

> The endpoint uses semantic search with FAISS (LangChain) and context expansion to retrieve neighboring chunks and improve response coherence.

## 📖 API Documentation

Once the server is running in development mode, access:

* Swagger UI: `http://localhost:8000/api/docs`
* ReDoc: `http://localhost:8000/api/redoc`

> **Note:** In production mode, API documentation is disabled for security reasons.

## 🏗️ Project Structure

```bash
.
├── app/
│   ├── llm/              # Groq LLM client
│   ├── rag/              # RAG system (embeddings, FAISS LangChain, retriever)
│   ├── routes/           # API endpoints
│   ├── main.py           # Main configuration
│   └── schemas.py        # Data models
├── venv/                 # Virtual environment
├── requirements.txt      # Dependencies
├── render.yaml           # Render deployment configuration
└── .env.example          # Environment variable template
```

## 🔒 Production Security

* Automatic API documentation disabled in production
* CORS configured with specific origins
* Structured logging
* Global error handling
* Environment variables for sensitive data

## 🛠️ Development

Run the application in development mode with auto-reload:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## 📝 License

See the LICENSE file for more details.

## 🤝 Contributing

Contributions are welcome. Please follow these steps:

1. Fork the project
2. Create your feature branch:

```bash
git checkout -b feature/AmazingFeature
```

3. Commit your changes:

```bash
git commit -m 'Add some AmazingFeature'
```

4. Push to the branch:

```bash
git push origin feature/AmazingFeature
```

5. Open a Pull Request

For questions or suggestions, please open an issue in the repository.

