# AI Knowledge Assistant - Mini RAG API

API de inteligencia artificial para consultas sobre documentos utilizando RAG (Retrieval-Augmented Generation).

## 🚀 Características

- Procesamiento y análisis de documentos **multi‑formato** (`.txt`, `.pdf`, `.docx`, `.md`, `.csv`, `.xlsx`, `.xls`)
- Sistema de embeddings con **Sentence Transformers** (vía `HuggingFaceEmbeddings`)
- Búsqueda semántica con **FAISS** (vectorstore de LangChain)
- Generación de respuestas con **Groq LLM**
- API RESTful con **FastAPI**
- Retrieval con expansión de contexto para mejorar la coherencia de las respuestas

## 📋 Requisitos

- Python 3.12+
- pip

> La API key de **Groq** (`GROQ_API_KEY`) se puede obtener de forma gratuita
> creando una cuenta en la consola de Groq: [Groq Console](https://console.groq.com/keys).

## 🛠️ Instalación Local

1. Clona el repositorio:
```bash
git clone <repository-url>
cd "AI Knowledge Assistant (Mini-RAG API)"
```

2. Crea y activa el entorno virtual:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

4. Configura las variables de entorno:
```bash
cp .env.example .env
# Edita .env con tus valores
```

5. Inicia el servidor:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

La API estará disponible en `http://localhost:8000`

### Variables de Entorno Requeridas

| Variable        | Descripción                                         | Requerida                    |
|----------------|-----------------------------------------------------|------------------------------|
| `ENV`          | Entorno de ejecución (`development` o `production`) | No (default: `development`)  |
| `GROQ_API_KEY` | API Key de Groq para el LLM                         | Sí                           |
| `FRONTEND_URL` | URL del frontend en producción                      | Sí (solo en producción)      |
| `ALLOWED_ORIGINS` | Orígenes permitidos para CORS (separados por coma) | No                         |

## 📚 Endpoints Principales

### Health Check
```
GET /api/health
```

### Subir Documento
```
POST /api/upload
Content-Type: multipart/form-data
Body: file (documento a procesar)
```

### Hacer Pregunta
```
POST /api/ask
Content-Type: application/json
Body: {
  "question": "tu pregunta aquí",
  "k": 5            // opcional, nº de chunks a recuperar (default: 5)
}
```

> El endpoint usa búsqueda semántica con FAISS (LangChain) y expansión de contexto
> para recuperar chunks vecinos y mejorar la coherencia de las respuestas.

## 📖 Documentación API

Una vez iniciado el servidor en modo desarrollo, accede a:
- Swagger UI: `http://localhost:8000/api/docs`
- ReDoc: `http://localhost:8000/api/redoc`

> **Nota**: En producción, la documentación está deshabilitada por seguridad.

## 🏗️ Estructura del Proyecto

```
.
├── app/
│   ├── llm/              # Cliente de Groq LLM
│   ├── rag/              # Sistema RAG (embeddings, FAISS LangChain, retriever)
│   ├── routes/           # Endpoints de la API
│   ├── main.py           # Configuración principal
│   └── schemas.py        # Modelos de datos
├── venv/                 # Entorno virtual
├── requirements.txt      # Dependencias
├── render.yaml          # Configuración de Render
└── .env.example         # Template de variables de entorno
```

## 🔒 Seguridad en Producción

- Documentación automática deshabilitada en producción
- CORS configurado con orígenes específicos
- Logging estructurado
- Manejo global de errores
- Variables de entorno para datos sensibles

## 🛠️ Desarrollo

Para ejecutar en modo desarrollo con recarga automática:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## 📝 Licencia

Ver archivo LICENSE

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor:
1. Fork el proyecto
2. Crea tu rama de feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📧 Contacto

Para preguntas o sugerencias, por favor abre un issue en el repositorio.# AI-doc-Assistant
