import streamlit as st
import requests
import time
from streamlit.components.v1 import html

BASE_API_URL = "http://127.0.0.1:8082"

st.set_page_config(
    page_title="AI Document Chat Assistant",
    layout="wide",
    page_icon="🤖",
    initial_sidebar_state="expanded"
)

# ------------------------
# SESSION STATE
# ------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "session_id" not in st.session_state:
    st.session_state.session_id = None

# ------------------------
# 🎨 ADVANCED DARK THEME WITH GRADIENTS
# ------------------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%);
        color: white;
    }
    .glass {
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
        border-radius: 20px;
        padding: 25px;
        margin: 10px 0;
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    }
    .header {
        text-align: center;
        background: linear-gradient(45deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3em;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .subheader {
        text-align: center;
        color: #b0b0b0;
        font-size: 1.2em;
    }
    .chat-bubble-user {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        padding: 15px;
        border-radius: 15px 15px 5px 15px;
        margin: 10px 0;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    .chat-bubble-assistant {
        background: rgba(255,255,255,0.1);
        color: white;
        padding: 15px;
        border-radius: 15px 15px 15px 5px;
        margin: 10px 0;
        border: 1px solid rgba(255,255,255,0.2);
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .stButton>button {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 10px 20px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
    }
    .stFileUploader {
        background: rgba(255,255,255,0.1);
        border: 2px dashed rgba(255,255,255,0.3);
        border-radius: 15px;
        padding: 20px;
    }
    .stSlider {
        color: white;
    }
    .sidebar {
        background: rgba(0,0,0,0.5);
        padding: 20px;
        border-radius: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------------
# SIDEBAR
# ------------------------
with st.sidebar:
    st.markdown("<div class='sidebar'>", unsafe_allow_html=True)
    st.markdown("## ⚙️ Settings")
    st.markdown("---")
    k = st.slider("🔍 Retrieval Chunks (k)", 1, 20, 5, help="Number of document chunks to retrieve")
    st.markdown("---")
    if st.button("🧹 Clear Chat History"):
        st.session_state.messages = []
        st.session_state.session_id = None
        st.success("Chat cleared!")
    st.markdown("---")
    st.markdown("### 📊 Stats")
    if st.session_state.session_id:
        st.write(f"Session ID: {st.session_state.session_id}")
    st.write(f"Messages: {len(st.session_state.messages)}")
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------------
# HEADER
# ------------------------
st.markdown(
    """
    <div class='glass'>
    <h1 class='header'>🤖 AI Document Chat Assistant</h1>
    <p class='subheader'>Upload documents and engage in intelligent conversations powered by AI</p>
    </div>
    """,
    unsafe_allow_html=True
)

# ------------------------
# 📂 MAIN UPLOAD SECTION
# ------------------------
st.markdown("<div class='glass'>", unsafe_allow_html=True)
st.markdown("### 📤 Upload Documents")
uploaded_files = st.file_uploader(
    "Select files to upload (PDF, DOCX, TXT, MD, CSV, XLSX)",
    type=["txt", "pdf", "docx", "md", "csv", "xlsx", "xls"],
    accept_multiple_files=True,
    help="Upload multiple documents to index and chat with"
)

col1, col2 = st.columns([1, 1])

with col1:
    upload_btn = st.button("🚀 Upload & Index Documents", use_container_width=True)

with col2:
    if st.button("📋 View Collections", use_container_width=True):
        try:
            res = requests.get(f"{BASE_API_URL}/api/collections")
            if res.status_code == 200:
                collections = res.json()
                st.info(f"Available Collections: {', '.join(collections) if collections else 'None'}")
            else:
                st.error("Failed to fetch collections")
        except:
            st.error("Backend not available")

st.markdown("</div>", unsafe_allow_html=True)

# ------------------------
# UPLOAD LOGIC
# ------------------------
if upload_btn:
    if not uploaded_files:
        st.error("⚠️ Please upload at least one file")
    else:
        files = []
        for file in uploaded_files:
            files.append(("files", (file.name, file.read(), file.type or "application/octet-stream")))

        progress_bar = st.progress(0)
        status_text = st.empty()

        with st.spinner("🔄 Processing documents..."):
            try:
                status_text.text("Uploading files...")
                progress_bar.progress(25)
                
                res = requests.post(f"{BASE_API_URL}/api/upload", files=files)
                progress_bar.progress(75)
                
                if res.status_code == 200:
                    data = res.json()
                    progress_bar.progress(100)
                    status_text.text("")
                    st.success(f"✅ Successfully indexed {data.get('documents_indexed', 0)} documents!")
                    time.sleep(1)
                    progress_bar.empty()
                    status_text.empty()
                else:
                    st.error(f"❌ Upload failed: {res.text}")
                    progress_bar.empty()
                    status_text.empty()
            except Exception as e:
                st.error(f"❌ Backend error: {e}")
                progress_bar.empty()
                status_text.empty()

# ------------------------
# CHAT UI
# ------------------------
st.markdown("<div class='glass'>", unsafe_allow_html=True)
st.markdown("### 💬 Chat Interface")

if len(st.session_state.messages) == 0:
    st.info("👆 Upload documents above and start asking questions!")

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div class='chat-bubble-user'>{msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-bubble-assistant'>{msg['content']}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ------------------------
# CHAT INPUT
# ------------------------
if prompt := st.chat_input("💭 Ask a question about your documents..."):
    st.markdown(f"<div class='chat-bubble-user'>{prompt}</div>", unsafe_allow_html=True)
    st.session_state.messages.append({"role": "user", "content": prompt})

    payload = {"question": prompt, "k": k}

    if st.session_state.session_id:
        payload["session_id"] = st.session_state.session_id

    with st.chat_message("assistant"):
        with st.spinner("🤔 AI is thinking..."):
            try:
                response = requests.post(
                    f"{BASE_API_URL}/api/ask",
                    json=payload,
                    timeout=120
                )

                if response.status_code == 200:
                    data = response.json()

                    st.session_state.session_id = data.get("session_id")
                    answer = data.get("answer", "No answer received")

                    # Typing effect
                    placeholder = st.empty()
                    full_text = ""
                    words = answer.split()
                    
                    for i, word in enumerate(words):
                        full_text += word + " "
                        if (i + 1) % 10 == 0 or i == len(words) - 1:
                            placeholder.markdown(f"<div class='chat-bubble-assistant'>{full_text}</div>", unsafe_allow_html=True)
                            time.sleep(0.05)

                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": answer
                    })

                    with st.expander("🔍 View Retrieved Chunks"):
                        st.write("**Question:**", data.get("question"))
                        if data.get("results"):
                            st.write("**Top Retrieved Chunks:**")
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
                error_msg = "⏰ Request timed out. The AI might be processing a complex query."
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})
            except Exception as e:
                error_msg = f"❌ Backend not running or connection error: {str(e)}"
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})

# ------------------------
# FOOTER
# ------------------------
st.markdown("---")
st.markdown(
    "<center><small style='color: #888;'>Powered by FastAPI, LangChain & Streamlit | Built with ❤️ for AI Document Assistance</small></center>",
    unsafe_allow_html=True
)