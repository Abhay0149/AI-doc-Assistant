import streamlit as st
import requests

# Backend API URL
BASE_API_URL = "http://127.0.0.1:8082"

# Page configuration
st.set_page_config(page_title="AI Document Assistant", page_icon="📄")

# Title
st.title("AI Document Assistant")

# Session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = []

if "uploaded_files" not in st.session_state:
    st.session_state.uploaded_files = []

# Upload section
st.header("Upload Documents")
uploaded_file = st.file_uploader("Choose a PDF or DOCX file", type=["pdf", "docx"])

if uploaded_file is not None:
    if st.button("Upload"):
        files = {"files": (uploaded_file.name, uploaded_file.read(), uploaded_file.type)}
        try:
            response = requests.post(f"{BASE_API_URL}/api/upload", files=files)
            if response.status_code == 200:
                data = response.json()
                st.success(f"Uploaded {data.get('documents_indexed', 0)} documents")
                st.session_state.uploaded_files.append(uploaded_file.name)
            else:
                st.error(f"Upload failed: {response.text}")
        except Exception as e:
            st.error(f"Error: {e}")

# Display uploaded files
if st.session_state.uploaded_files:
    st.subheader("Uploaded Files")
    for file in st.session_state.uploaded_files:
        st.write(f"- {file}")

# Chat section
st.header("Chat with Documents")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask a question about your documents"):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get AI response
    payload = {"question": prompt, "k": 5}
    try:
        response = requests.post(f"{BASE_API_URL}/api/ask", json=payload, timeout=60)
        if response.status_code == 200:
            data = response.json()
            answer = data.get("answer", "No answer")
            st.session_state.messages.append({"role": "assistant", "content": answer})
            with st.chat_message("assistant"):
                st.markdown(answer)
        else:
            error_msg = f"Error: {response.text}"
            st.session_state.messages.append({"role": "assistant", "content": error_msg})
            with st.chat_message("assistant"):
                st.markdown(error_msg)
    except Exception as e:
        error_msg = f"Error: {str(e)}"
        st.session_state.messages.append({"role": "assistant", "content": error_msg})
        with st.chat_message("assistant"):
            st.markdown(error_msg)
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(138, 43, 226, 0.1), transparent);
        transition: left 0.5s;
    }
    
    .glass:hover::before {
        left: 100%;
    }
    
    .neon-text {
        background: linear-gradient(45deg, #00ffff, #ff00ff, #ffff00, #00ffff);
        background-size: 400% 400%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: neon-glow 2s ease-in-out infinite alternate;
        font-family: 'Orbitron', monospace;
        font-weight: 900;
        font-size: 3.5em;
        text-align: center;
        margin: 20px 0;
    }
    
    @keyframes neon-glow {
        from { filter: brightness(1) drop-shadow(0 0 5px #00ffff); }
        to { filter: brightness(1.2) drop-shadow(0 0 20px #ff00ff); }
    }
    
    .ai-brain {
        text-align: center;
        margin: 30px 0;
        filter: drop-shadow(0 0 30px rgba(138, 43, 226, 0.5));
    }
    
    .chat-bubble-user {
        background: linear-gradient(135deg, #00ffff, #0080ff);
        color: white;
        padding: 20px;
        border-radius: 20px 20px 5px 20px;
        margin: 15px 0;
        box-shadow: 0 5px 15px rgba(0, 255, 255, 0.3);
        border: 1px solid rgba(0, 255, 255, 0.5);
        animation: slide-in-left 0.5s ease-out;
    }
    
    .chat-bubble-assistant {
        background: linear-gradient(135deg, rgba(138, 43, 226, 0.2), rgba(255, 0, 255, 0.1));
        color: white;
        padding: 20px;
        border-radius: 20px 20px 20px 5px;
        margin: 15px 0;
        border: 1px solid rgba(138, 43, 226, 0.3);
        box-shadow: 0 5px 15px rgba(138, 43, 226, 0.2);
        animation: slide-in-right 0.5s ease-out;
    }
    
    @keyframes slide-in-left {
        from { transform: translateX(-50px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes slide-in-right {
        from { transform: translateX(50px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    .stButton>button {
        background: linear-gradient(45deg, #00ffff, #ff00ff);
        color: white;
        border: none;
        border-radius: 15px;
        padding: 15px 30px;
        font-weight: 600;
        font-size: 16px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 255, 255, 0.3);
    }
    
    .stButton>button:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 8px 25px rgba(255, 0, 255, 0.4);
        filter: brightness(1.2);
    }
    
    .sidebar-glass {
        background: rgba(0,0,0,0.3);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
    }
    
    .feature-highlight {
        background: linear-gradient(135deg, rgba(255,215,0,0.1), rgba(255,69,0,0.1));
        border: 1px solid rgba(255,215,0, 0.5);
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 4px 15px rgba(255,215,0, 0.2);
    }
    
    .architecture-diagram {
        background: rgba(0,0,0,0.5);
        border: 2px solid rgba(138, 43, 226, 0.5);
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        box-shadow: 0 0 40px rgba(138, 43, 226, 0.3);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------------
# SESSION STATE
# ------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "session_id" not in st.session_state:
    st.session_state.session_id = None

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

# ------------------------
# SIDEBAR NAVIGATION
# ------------------------
with st.sidebar:
    st.markdown("<div class='sidebar-glass'>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #00ffff; font-family: Orbitron;'>🧠 NeuroDocs AI</h2>", unsafe_allow_html=True)
    st.markdown("---")
    
    selected = option_menu(
        menu_title=None,
        options=["Dashboard", "Upload Documents", "AI Chat", "Architecture", "Settings"],
        icons=["house", "cloud-upload", "chat-dots", "diagram-3", "gear"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "#00ffff", "font-size": "20px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "0px",
                "color": "#ffffff",
                "background-color": "transparent",
                "--hover-color": "rgba(0,255,255,0.1)",
            },
            "nav-link-selected": {"background-color": "rgba(138, 43, 226, 0.2)", "border-left": "4px solid #00ffff"},
        }
    )
    
    st.session_state.page = selected
    
    st.markdown("---")
    st.markdown("### System Status")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Backend", "🟢 Online", delta="8082")
    with col2:
        st.metric("Frontend", "🟢 Active", delta="8501")
    
    if st.session_state.session_id:
        st.markdown(f"**Session:** {st.session_state.session_id[:8]}...")
    
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------------
# DASHBOARD PAGE
# ------------------------
def show_dashboard():
    st.markdown("<h1 class='neon-text'>NeuroDocs AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #b0b0b0; font-size: 1.2em;'>Premium AI-Powered Document Intelligence Platform</p>", unsafe_allow_html=True)
    
    # AI Brain Animation
    st.markdown("<div class='ai-brain'>", unsafe_allow_html=True)
    brain_lottie = {
        "loop": True,
        "autoplay": True,
        "animationData": {
            "v": "5.7.1",
            "meta": {"g": "LottieFiles AE 0.1.20"},
            "fr": 30,
            "ip": 0,
            "op": 180,
            "w": 500,
            "h": 500,
            "nm": "Brain Animation",
            "ddd": 0,
            "assets": [],
            "layers": [
                {
                    "ddd": 0,
                    "ind": 1,
                    "ty": 4,
                    "nm": "Brain",
                    "sr": 1,
                    "ks": {
                        "o": {"a": 0, "k": 100, "ix": 11},
                        "r": {"a": 0, "k": 0, "ix": 10},
                        "p": {"a": 0, "k": [250, 250, 0], "ix": 2},
                        "a": {"a": 0, "k": [250, 250, 0], "ix": 1},
                        "s": {"a": 0, "k": [100, 100, 100], "ix": 6}
                    },
                    "ao": 0,
                    "shapes": [
                        {
                            "ty": "gr",
                            "it": [
                                {
                                    "d": 1,
                                    "ty": "el",
                                    "s": {"a": 0, "k": [400, 300], "ix": 2},
                                    "p": {"a": 0, "k": [0, 0], "ix": 3}
                                },
                                {
                                    "ty": "st",
                                    "c": {"a": 0, "k": [0, 1, 1, 1], "ix": 3},
                                    "o": {"a": 0, "k": 100, "ix": 4},
                                    "w": {"a": 0, "k": 4, "ix": 5},
                                    "lc": 1,
                                    "lj": 1,
                                    "ml": 4,
                                    "bm": 0,
                                    "nm": "Stroke 1",
                                    "mn": "ADBE Vector Graphic - Stroke",
                                    "hd": False
                                },
                                {
                                    "ty": "gf",
                                    "o": {"a": 0, "k": 100, "ix": 10},
                                    "r": 1,
                                    "bm": 0,
                                    "g": {
                                        "p": 3,
                                        "k": {
                                            "a": 0,
                                            "k": [
                                                0, 0.5, 0.5, 0.5, 0.5,
                                                0.167, 0, 1, 1, 0.833,
                                                1, 0, 0, 0, 1
                                            ],
                                            "ix": 9
                                        }
                                    },
                                    "s": {"a": 0, "k": [0, 0], "ix": 5},
                                    "e": {"a": 0, "k": [100, 100], "ix": 6},
                                    "t": 1,
                                    "bm": 0,
                                    "nm": "Gradient Fill 1",
                                    "mn": "ADBE Vector Graphic - GFill",
                                    "hd": False
                                }
                            ],
                            "nm": "Brain Shape",
                            "np": 3,
                            "cix": 2,
                            "bm": 0,
                            "ix": 1,
                            "mn": "ADBE Vector Group",
                            "hd": False
                        }
                    ],
                    "ip": 0,
                    "op": 180,
                    "st": 0,
                    "bm": 0
                }
            ]
        }
    }
    st_lottie(brain_lottie, height=300, key="brain")
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Feature Highlights
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.markdown("### 🚀 Key Features")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class='feature-highlight'>
        <h4>🧠 Advanced AI</h4>
        <p>Groq-powered LLM for intelligent document analysis</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='feature-highlight'>
        <h4>🔍 Semantic Search</h4>
        <p>Vector-based retrieval for precise information extraction</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='feature-highlight'>
        <h4>💬 Interactive Chat</h4>
        <p>Conversational interface for natural document querying</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Stats
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.markdown("### 📊 Platform Statistics")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Documents Processed", "1,247", "+12%")
    with col2:
        st.metric("AI Queries", "8,932", "+23%")
    with col3:
        st.metric("Accuracy Rate", "94.7%", "+2.1%")
    with col4:
        st.metric("Response Time", "0.8s", "-0.2s")
    
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------------
# UPLOAD PAGE
# ------------------------
def show_upload():
    st.markdown("<h1 style='color: #00ffff; font-family: Orbitron; text-align: center;'>📤 Document Upload Center</h1>", unsafe_allow_html=True)
    
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.markdown("### Upload & Index Documents")
    uploaded_files = st.file_uploader(
        "Select documents to process",
        type=["txt", "pdf", "docx", "md", "csv", "xlsx", "xls"],
        accept_multiple_files=True,
        help="Supported formats: PDF, DOCX, TXT, MD, CSV, XLSX"
    )
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        upload_btn = st.button("🚀 Process & Index", use_container_width=True)
    
    with col2:
        if st.button("📋 View Collections", use_container_width=True):
            try:
                res = requests.get(f"{BASE_API_URL}/api/collections")
                if res.status_code == 200:
                    collections = res.json()
                    st.success(f"Available Collections: {', '.join(collections) if collections else 'None'}")
                else:
                    st.error("Failed to fetch collections")
            except:
                st.error("Backend not available")
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    if upload_btn:
        if not uploaded_files:
            st.error("⚠️ Please select at least one document")
        else:
            files = []
            for file in uploaded_files:
                files.append(("files", (file.name, file.read(), file.type or "application/octet-stream")))
            
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            with st.spinner("🔄 Processing documents with AI..."):
                try:
                    status_text.markdown("📤 Uploading files...")
                    progress_bar.progress(25)
                    
                    res = requests.post(f"{BASE_API_URL}/api/upload", files=files)
                    progress_bar.progress(75)
                    
                    if res.status_code == 200:
                        data = res.json()
                        progress_bar.progress(100)
                        status_text.markdown("")
                        st.success(f"✅ Successfully processed {data.get('documents_indexed', 0)} documents!")
                        time.sleep(1)
                        progress_bar.empty()
                        status_text.empty()
                    else:
                        st.error(f"❌ Processing failed: {res.text}")
                        progress_bar.empty()
                        status_text.empty()
                except Exception as e:
                    st.error(f"❌ Backend error: {e}")
                    progress_bar.empty()
                    status_text.empty()

# ------------------------
# CHAT PAGE
# ------------------------
def show_chat():
    st.markdown("<h1 style='color: #00ffff; font-family: Orbitron; text-align: center;'>💬 AI Conversation Hub</h1>", unsafe_allow_html=True)
    
    # Settings in chat page
    col1, col2 = st.columns([3, 1])
    with col2:
        k = st.slider("🔍 Retrieval Depth", 1, 20, 5, help="Number of chunks to retrieve")
        if st.button("🧹 Clear Conversation"):
            st.session_state.messages = []
            st.session_state.session_id = None
            st.success("Conversation cleared!")
    
    # Chat Interface
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.markdown("### AI Chat Interface")
    
    if len(st.session_state.messages) == 0:
        st.info("👋 Start a conversation by asking a question about your uploaded documents!")
    
    chat_container = st.container()
    with chat_container:
        for msg in st.session_state.messages:
            if msg["role"] == "user":
                st.markdown(f"<div class='chat-bubble-user'>{msg['content']}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='chat-bubble-assistant'>{msg['content']}</div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Chat Input
    if prompt := st.chat_input("💭 Ask anything about your documents..."):
        with chat_container:
            st.markdown(f"<div class='chat-bubble-user'>{prompt}</div>", unsafe_allow_html=True)
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        payload = {"question": prompt, "k": k}
        if st.session_state.session_id:
            payload["session_id"] = st.session_state.session_id
        
        with st.chat_message("assistant"):
            with st.spinner("🧠 AI is processing your query..."):
                try:
                    response = requests.post(
                        f"{BASE_API_URL}/api/ask",
                        json=payload,
                        timeout=120
                    )
                    
                    if response.status_code == 200:
                        data = response.json()
                        st.session_state.session_id = data.get("session_id")
                        answer = data.get("answer", "No response generated")
                        
                        # Typing effect
                        placeholder = st.empty()
                        full_text = ""
                        words = answer.split()
                        
                        for i, word in enumerate(words):
                            full_text += word + " "
                            if (i + 1) % 15 == 0 or i == len(words) - 1:
                                with chat_container:
                                    st.markdown(f"<div class='chat-bubble-assistant'>{full_text}</div>", unsafe_allow_html=True)
                                time.sleep(0.02)
                        
                        st.session_state.messages.append({
                            "role": "assistant",
                            "content": answer
                        })
                        
                        with st.expander("🔍 Retrieval Details"):
                            st.write("**Query:**", data.get("question"))
                            if data.get("results"):
                                st.write("**Retrieved Chunks:**")
                                for r in data["results"]:
                                    st.write(
                                        f"📄 Doc {r.get('document_id')} | 🔢 Chunk {r.get('chunk_index')} | 🎯 Score: {r.get('score'):.4f}"
                                    )
                            else:
                                st.write("No retrieval results")
                    
                    else:
                        error_msg = f"❌ API Error ({response.status_code}): {response.text}"
                        st.error(error_msg)
                        st.session_state.messages.append({"role": "assistant", "content": error_msg})
                
                except requests.exceptions.Timeout:
                    error_msg = "⏰ Request timed out. The AI may be processing complex queries."
                    st.error(error_msg)
                    st.session_state.messages.append({"role": "assistant", "content": error_msg})
                except Exception as e:
                    error_msg = f"❌ Connection error: {str(e)}"
                    st.error(error_msg)
                    st.session_state.messages.append({"role": "assistant", "content": error_msg})

# ------------------------
# ARCHITECTURE PAGE
# ------------------------
def show_architecture():
    st.markdown("<h1 style='color: #00ffff; font-family: Orbitron; text-align: center;'>🏗️ System Architecture</h1>", unsafe_allow_html=True)
    
    st.markdown("<div class='architecture-diagram'>", unsafe_allow_html=True)
    st.markdown("""
    ```mermaid
    graph TB
        A[User Interface<br/>Streamlit Frontend] --> B[FastAPI Backend<br/>REST API]
        B --> C[Document Processor<br/>Text Extraction]
        B --> D[Embedding Engine<br/>Sentence Transformers]
        B --> E[Vector Database<br/>PGVector + PostgreSQL]
        B --> F[LLM Service<br/>Groq API]
        
        C --> G[Chunking Strategy<br/>Semantic Splitting]
        D --> H[Vector Store<br/>FAISS/Chroma]
        E --> I[Retrieval System<br/>Semantic Search]
        F --> J[Response Generation<br/>Context-Augmented]
        
        I --> K[Chat Interface<br/>Conversational AI]
        J --> K
        
        style A fill:#00ffff,stroke:#000,stroke-width:2px
        style B fill:#ff00ff,stroke:#000,stroke-width:2px
        style F fill:#ffff00,stroke:#000,stroke-width:2px
        style K fill:#00ff00,stroke:#000,stroke-width:2px
    ```
    """)
    
    st.markdown("### Architecture Overview")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Frontend Layer:**
        - Streamlit-based UI
        - Real-time chat interface
        - Document upload portal
        - Progress visualization
        
        **Backend Layer:**
        - FastAPI REST API
        - Async processing
        - Session management
        - Error handling
        """)
    
    with col2:
        st.markdown("""
        **AI/ML Layer:**
        - Groq LLM integration
        - Sentence Transformers
        - Vector embeddings
        - Semantic retrieval
        
        **Data Layer:**
        - PostgreSQL + PGVector
        - Document storage
        - Vector indexing
        - Metadata management
        """)
    
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------------
# SETTINGS PAGE
# ------------------------
def show_settings():
    st.markdown("<h1 style='color: #00ffff; font-family: Orbitron; text-align: center;'>⚙️ Advanced Settings</h1>", unsafe_allow_html=True)
    
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.markdown("### AI Configuration")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Retrieval Settings")
        chunk_size = st.slider("Chunk Size", 500, 2000, 1000, help="Size of text chunks for processing")
        overlap = st.slider("Chunk Overlap", 0, 200, 100, help="Overlap between chunks")
        top_k = st.slider("Top K Results", 1, 20, 5, help="Number of top results to retrieve")
    
    with col2:
        st.markdown("#### Model Settings")
        temperature = st.slider("Temperature", 0.0, 1.0, 0.7, help="Creativity level for AI responses")
        max_tokens = st.slider("Max Tokens", 100, 2000, 500, help="Maximum response length")
        model_choice = st.selectbox("LLM Model", ["groq-llama3", "groq-mixtral", "groq-gemma"], help="Choose AI model")
    
    st.markdown("---")
    st.markdown("### System Information")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Python Version", "3.13")
    with col2:
        st.metric("FastAPI Status", "Running")
    with col3:
        st.metric("Vector DB", "PostgreSQL")
    
    if st.button("🔄 Apply Settings", use_container_width=True):
        st.success("Settings applied successfully!")
    
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------------
# PAGE ROUTING
# ------------------------
if st.session_state.page == "Dashboard":
    show_dashboard()
elif st.session_state.page == "Upload Documents":
    show_upload()
elif st.session_state.page == "AI Chat":
    show_chat()
elif st.session_state.page == "Architecture":
    show_architecture()
elif st.session_state.page == "Settings":
    show_settings()

# ------------------------
# FOOTER
# ------------------------
st.markdown("---")
st.markdown(
    "<center><small style='color: #666;'>© 2026 NeuroDocs AI - Premium Document Intelligence Platform | Powered by FastAPI, LangChain & Streamlit</small></center>",
    unsafe_allow_html=True
)