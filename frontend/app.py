import requests
import streamlit as st


BASE_API_URL = "http://127.0.0.1:8082"


st.set_page_config(
    page_title="AI Document Assistant",
    page_icon="📄",
    layout="wide",
)


st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap');

        html, body, [class*="css"] {
            font-family: 'Manrope', sans-serif;
        }

        .stApp {
            background:
                radial-gradient(circle at top left, rgba(34, 211, 238, 0.12), transparent 30%),
                radial-gradient(circle at top right, rgba(129, 140, 248, 0.10), transparent 28%),
                linear-gradient(180deg, #030712 0%, #07111f 100%);
            color: #f8fafc;
        }

        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }

        .hero-panel,
        .visual-panel,
        .section-container {
            background: linear-gradient(145deg, rgba(8, 14, 27, 0.96), rgba(7, 11, 22, 0.88));
            border: 1px solid rgba(148, 163, 184, 0.14);
            border-radius: 24px;
            box-shadow: 0 24px 60px rgba(2, 6, 23, 0.35);
        }

        .hero-panel {
            padding: 2.8rem;
        }

        .visual-panel {
            min-height: 100%;
            padding: 2rem;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .eyebrow {
            display: inline-flex;
            align-items: center;
            gap: 0.55rem;
            padding: 0.48rem 0.85rem;
            margin-bottom: 1.2rem;
            border-radius: 999px;
            border: 1px solid rgba(56, 189, 248, 0.20);
            background: rgba(15, 23, 42, 0.78);
            color: #c7d2fe;
            font-size: 0.8rem;
            font-weight: 700;
            letter-spacing: 0.12em;
            text-transform: uppercase;
        }

        .eyebrow-dot {
            width: 8px;
            height: 8px;
            border-radius: 999px;
            background: linear-gradient(135deg, #22d3ee, #818cf8);
            box-shadow: 0 0 12px rgba(34, 211, 238, 0.8);
        }

        .main-title {
            margin: 0 0 1rem 0;
            font-size: clamp(3rem, 5vw, 4.7rem);
            font-weight: 800;
            line-height: 1.02;
            letter-spacing: -0.05em;
            background: linear-gradient(92deg, #f8fafc 0%, #ddd6fe 28%, #67e8f9 58%, #f8fafc 100%);
            background-size: 220% 220%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: titleGlow 8s ease infinite;
        }

        .hero-accent {
            display: block;
        }

        .welcome-text {
            margin: 0 0 1.6rem 0;
            max-width: 680px;
            color: #cbd5e1;
            font-size: 1.05rem;
            line-height: 1.8;
        }

        .feature-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 0.9rem;
            margin: 0 0 1.2rem 0;
        }

        .feature-card {
            padding: 1rem;
            border-radius: 18px;
            background: rgba(15, 23, 42, 0.70);
            border: 1px solid rgba(148, 163, 184, 0.12);
            transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
        }

        .feature-card:hover {
            transform: translateY(-3px);
            border-color: rgba(103, 232, 249, 0.32);
            box-shadow: 0 14px 30px rgba(8, 47, 73, 0.22);
        }

        .feature-kicker {
            color: #67e8f9;
            font-size: 0.8rem;
            font-weight: 800;
            letter-spacing: 0.08em;
            margin-bottom: 0.45rem;
        }

        .feature-title {
            color: #f8fafc;
            font-size: 1rem;
            font-weight: 700;
            margin-bottom: 0.3rem;
        }

        .feature-copy {
            color: #94a3b8;
            font-size: 0.88rem;
            line-height: 1.5;
        }

        .hero-note {
            color: #7dd3fc;
            font-size: 0.92rem;
            margin-top: 0.8rem;
        }

        .visual-stack {
            position: relative;
            width: min(380px, 78vw);
            aspect-ratio: 1;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .visual-ring {
            position: absolute;
            inset: 0;
            border-radius: 50%;
            border: 1px solid rgba(103, 232, 249, 0.16);
        }

        .visual-ring.inner {
            inset: 12%;
            border-color: rgba(129, 140, 248, 0.18);
        }

        .visual-orb {
            width: 64%;
            aspect-ratio: 1;
            border-radius: 50%;
            background:
                radial-gradient(circle at 35% 35%, rgba(255, 255, 255, 0.95), rgba(255,255,255,0.16) 16%, transparent 19%),
                radial-gradient(circle at center, rgba(103, 232, 249, 0.78), rgba(129, 140, 248, 0.44) 45%, rgba(15, 23, 42, 0.05) 70%, transparent 72%);
            box-shadow:
                0 0 70px rgba(34, 211, 238, 0.24),
                0 0 120px rgba(129, 140, 248, 0.14);
            animation: floatOrb 6s ease-in-out infinite;
        }

        .visual-tag {
            position: absolute;
            bottom: 6%;
            padding: 0.7rem 1rem;
            border-radius: 999px;
            border: 1px solid rgba(148, 163, 184, 0.18);
            background: rgba(15, 23, 42, 0.78);
            color: #cbd5e1;
            font-size: 0.9rem;
            font-weight: 600;
        }

        .section-container {
            padding: 1.8rem;
            margin: 1rem 0;
        }

        .upload-section {
            margin-bottom: 1.2rem;
        }

        .workspace-header {
            margin-bottom: 1.6rem;
        }

        .workspace-kicker {
            display: inline-flex;
            align-items: center;
            gap: 0.55rem;
            padding: 0.5rem 1rem;
            border-radius: 999px;
            border: 1px solid rgba(148, 163, 184, 0.12);
            background: linear-gradient(135deg, rgba(15, 23, 42, 0.72), rgba(15, 23, 42, 0.48));
            color: #cbd5e1;
            font-size: 0.78rem;
            font-weight: 600;
            letter-spacing: 0.14em;
            text-transform: uppercase;
            margin-bottom: 1.7rem;
            backdrop-filter: blur(14px);
            -webkit-backdrop-filter: blur(14px);
            box-shadow:
                inset 0 1px 0 rgba(255, 255, 255, 0.05),
                0 10px 30px rgba(15, 23, 42, 0.18),
                0 0 0 1px rgba(99, 102, 241, 0.04);
            position: relative;
            overflow: hidden;
            transform-origin: left center;
            transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
        }

        .workspace-kicker::before {
            content: "";
            position: absolute;
            inset: 0;
            padding: 1px;
            border-radius: inherit;
            background: linear-gradient(120deg, rgba(103, 232, 249, 0.22), rgba(129, 140, 248, 0.16), rgba(255, 255, 255, 0.04));
            -webkit-mask:
                linear-gradient(#fff 0 0) content-box,
                linear-gradient(#fff 0 0);
            -webkit-mask-composite: xor;
            mask-composite: exclude;
            pointer-events: none;
        }

        .workspace-kicker:hover {
            transform: scale(1.02);
            border-color: rgba(103, 232, 249, 0.16);
            box-shadow:
                inset 0 1px 0 rgba(255, 255, 255, 0.06),
                0 14px 38px rgba(15, 23, 42, 0.24),
                0 0 24px rgba(103, 232, 249, 0.08);
        }

        .workspace-title {
            margin: 0 0 0.95rem 0;
            font-size: clamp(2.7rem, 4.6vw, 4.2rem);
            font-weight: 800;
            letter-spacing: -0.05em;
            line-height: 1.04;
            background: linear-gradient(90deg, #f8fafc 0%, #7dd3fc 42%, #c4b5fd 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .workspace-subtitle {
            margin: 0;
            color: #94a3b8;
            font-size: 1rem;
            line-height: 1.75;
            max-width: 760px;
        }

        .metric-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 0.9rem;
            margin: 1.4rem 0 1rem;
        }

        .metric-card {
            padding: 1rem 1.1rem;
            border-radius: 18px;
            background: rgba(15, 23, 42, 0.62);
            border: 1px solid rgba(148, 163, 184, 0.12);
            box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.03);
            transition: transform 0.2s ease, border-color 0.2s ease;
        }

        .metric-card:hover {
            transform: translateY(-2px);
            border-color: rgba(103, 232, 249, 0.28);
        }

        .metric-label {
            color: #94a3b8;
            font-size: 0.8rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
        }

        .metric-value {
            margin-top: 0.45rem;
            color: #f8fafc;
            font-size: 1.08rem;
            font-weight: 700;
        }

        .panel-heading {
            display: flex;
            align-items: flex-start;
            justify-content: space-between;
            gap: 1rem;
            margin-bottom: 1.2rem;
        }

        .panel-title {
            margin: 0;
            color: #f8fafc;
            font-size: 1.5rem;
            font-weight: 800;
            letter-spacing: -0.03em;
        }

        .panel-copy {
            margin: 0.35rem 0 0;
            color: #94a3b8;
            font-size: 0.95rem;
            line-height: 1.6;
        }

        .panel-badge {
            padding: 0.45rem 0.8rem;
            border-radius: 999px;
            background: rgba(15, 23, 42, 0.82);
            border: 1px solid rgba(148, 163, 184, 0.15);
            color: #cbd5e1;
            font-size: 0.82rem;
            font-weight: 700;
            white-space: nowrap;
        }

        .upload-shell {
            padding: 1rem;
            border-radius: 20px;
            background:
                radial-gradient(circle at top left, rgba(34, 211, 238, 0.08), transparent 28%),
                rgba(2, 6, 23, 0.26);
            border: 1px dashed rgba(103, 232, 249, 0.18);
        }

        .upload-helper-row {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 0.8rem;
            margin-top: 1rem;
        }

        .helper-card {
            padding: 0.9rem 1rem;
            border-radius: 16px;
            background: rgba(15, 23, 42, 0.64);
            border: 1px solid rgba(148, 163, 184, 0.1);
        }

        .helper-title {
            color: #e2e8f0;
            font-size: 0.92rem;
            font-weight: 700;
            margin-bottom: 0.25rem;
        }

        .helper-copy {
            color: #94a3b8;
            font-size: 0.82rem;
            line-height: 1.55;
        }

        .chat-section {
            max-height: 60vh;
            overflow-y: auto;
        }

        .chat-empty {
            padding: 1.3rem;
            border-radius: 18px;
            background: rgba(15, 23, 42, 0.62);
            border: 1px solid rgba(148, 163, 184, 0.12);
            margin-bottom: 1rem;
        }

        .chat-empty-title {
            color: #f8fafc;
            font-size: 1rem;
            font-weight: 700;
            margin-bottom: 0.4rem;
        }

        .chat-empty-copy {
            color: #94a3b8;
            font-size: 0.92rem;
            line-height: 1.6;
        }

        .stButton > button {
            background: linear-gradient(135deg, #67e8f9, #818cf8 54%, #a78bfa) !important;
            color: #020617 !important;
            border: 1px solid rgba(255, 255, 255, 0.14) !important;
            border-radius: 999px !important;
            padding: 0.95rem 2.15rem !important;
            font-size: 1rem !important;
            font-weight: 800 !important;
            box-shadow: 0 18px 38px rgba(56, 189, 248, 0.20) !important;
            transition: transform 0.2s ease, box-shadow 0.2s ease !important;
        }

        .stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 22px 44px rgba(56, 189, 248, 0.26) !important;
        }

        .stFileUploader,
        .uploaded-files,
        .stChatMessage,
        .stChatInput,
        .sidebar .stRadio {
            background: rgba(15, 23, 42, 0.58);
            border-radius: 14px;
        }

        .stFileUploader {
            border: 1px dashed rgba(125, 211, 252, 0.22);
            padding: 1rem;
        }

        .uploaded-files {
            padding: 1rem;
            margin-top: 1rem;
        }

        .file-item {
            color: #cbd5e1;
            font-size: 0.95rem;
            padding: 0.25rem 0;
        }

        .stChatMessage {
            border: 1px solid rgba(148, 163, 184, 0.10);
            padding: 1rem;
        }

        .sidebar .stRadio {
            padding: 1rem;
        }

        @keyframes floatOrb {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }

        @keyframes titleGlow {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        @media (max-width: 1000px) {
            .feature-grid,
            .metric-grid,
            .upload-helper-row {
                grid-template-columns: 1fr;
            }
        }

        @media (max-width: 640px) {
            .hero-panel,
            .visual-panel,
            .section-container {
                padding: 1.4rem;
                border-radius: 20px;
            }

            .main-title {
                font-size: 2.6rem;
            }

            .workspace-kicker {
                margin-bottom: 1.35rem;
            }

            .visual-tag {
                position: static;
                margin-top: 1rem;
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)


if "messages" not in st.session_state:
    st.session_state.messages = []

if "uploaded_files" not in st.session_state:
    st.session_state.uploaded_files = []

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"


st.sidebar.title("Navigation")
page_options = ["Dashboard", "Browse / Chat"]
selected_page = st.sidebar.radio(
    "Go to",
    page_options,
    index=page_options.index(st.session_state.page),
    key="page_selector",
)

if selected_page != st.session_state.page:
    st.session_state.page = selected_page
    st.rerun()


if st.session_state.page == "Dashboard":
    col_left, col_right = st.columns([1.15, 0.85], gap="large")

    with col_left:
        st.markdown(
            """
            <div class="hero-panel">
                <div class="eyebrow"><span class="eyebrow-dot"></span>AI Knowledge Workspace</div>
                <h1 class="main-title">Transform static files into <span class="hero-accent">a high-signal AI research layer.</span></h1>
                <p class="welcome-text">
                    Turn dense PDFs and reports into an intelligent product experience. Upload your knowledge base,
                    retrieve the right evidence instantly, and ask natural questions with answers grounded in your documents.
                </p>
                <div class="feature-grid">
                    <div class="feature-card">
                        <div class="feature-kicker">01</div>
                        <div class="feature-title">Context-Aware Retrieval</div>
                        <div class="feature-copy">Surface the most relevant passages before generation.</div>
                    </div>
                    <div class="feature-card">
                        <div class="feature-kicker">02</div>
                        <div class="feature-title">Conversational Analysis</div>
                        <div class="feature-copy">Explore technical docs like a live product intelligence feed.</div>
                    </div>
                    <div class="feature-card">
                        <div class="feature-kicker">03</div>
                        <div class="feature-title">Fast Upload-to-Insight</div>
                        <div class="feature-copy">Move from ingestion to answers in a focused, low-friction flow.</div>
                    </div>
                </div>
                <div class="hero-note">Built for premium document search, synthesis, and discovery.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button("Start Exploring →", key="cta_button"):
            st.session_state.page = "Browse / Chat"
            st.rerun()

    with col_right:
        st.markdown(
            """
            <div class="visual-panel">
                <div class="visual-stack">
                    <div class="visual-ring"></div>
                    <div class="visual-ring inner"></div>
                    <div class="visual-orb"></div>
                    <div class="visual-tag">Retrieval • Synthesis • Answers</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

elif st.session_state.page == "Browse / Chat":
    uploaded_count = len(st.session_state.uploaded_files)
    chat_count = len(st.session_state.messages)
    workspace_state = "Ready for ingestion" if uploaded_count == 0 else "Knowledge base active"

    st.markdown(
        f"""
        <div class="workspace-header">
            <div class="workspace-kicker"><span class="eyebrow-dot"></span>AI Document Workspace</div>
            <h1 class="workspace-title">Browse, ingest, and converse with your knowledge base.</h1>
            <p class="workspace-subtitle">
                Move from static files to guided AI analysis. Upload premium source material, organize context,
                and ask grounded questions in a workspace designed for focused research.
            </p>
            <div class="metric-grid">
                <div class="metric-card">
                    <div class="metric-label">Workspace Status</div>
                    <div class="metric-value">{workspace_state}</div>
                </div>
                <div class="metric-card">
                    <div class="metric-label">Documents Indexed</div>
                    <div class="metric-value">{uploaded_count}</div>
                </div>
                <div class="metric-card">
                    <div class="metric-label">Conversation Turns</div>
                    <div class="metric-value">{chat_count}</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="section-container upload-section">', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="panel-heading">
            <div>
                <h2 class="panel-title">Upload Documents</h2>
                <p class="panel-copy">Bring in PDFs and DOCX files to create a richer retrieval layer for downstream answers.</p>
            </div>
            <div class="panel-badge">PDF + DOCX</div>
        </div>
        <div class="upload-shell">
        """,
        unsafe_allow_html=True,
    )

    uploaded_file = st.file_uploader(
        "Browse Files",
        type=["pdf", "docx"],
        label_visibility="collapsed",
    )

    if uploaded_file is not None:
        if st.button("Upload Document", use_container_width=True):
            with st.spinner("Uploading..."):
                files = {"files": (uploaded_file.name, uploaded_file.read(), uploaded_file.type)}
                try:
                    response = requests.post(f"{BASE_API_URL}/api/upload", files=files)
                    if response.status_code == 200:
                        data = response.json()
                        st.success(f"✅ Uploaded {data.get('documents_indexed', 0)} documents")
                        if uploaded_file.name not in st.session_state.uploaded_files:
                            st.session_state.uploaded_files.append(uploaded_file.name)
                    else:
                        st.error(f"❌ Upload failed: {response.text}")
                except Exception as exc:
                    st.error(f"❌ Error: {exc}")

    st.markdown(
        """
        <div class="upload-helper-row">
            <div class="helper-card">
                <div class="helper-title">High-signal retrieval</div>
                <div class="helper-copy">Index dense reports and reference docs for grounded, searchable answers.</div>
            </div>
            <div class="helper-card">
                <div class="helper-title">Fast onboarding</div>
                <div class="helper-copy">Move from file upload to exploration in one clean product flow.</div>
            </div>
            <div class="helper-card">
                <div class="helper-title">Conversation-ready</div>
                <div class="helper-copy">Once indexed, your knowledge base is ready for iterative AI analysis.</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.session_state.uploaded_files:
        st.markdown('<div class="uploaded-files">', unsafe_allow_html=True)
        st.write("**Uploaded Files:**")
        for file in st.session_state.uploaded_files:
            st.markdown(f'<div class="file-item">📄 {file}</div>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="section-container chat-section">', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="panel-heading">
            <div>
                <h2 class="panel-title">Chat with Documents</h2>
                <p class="panel-copy">Ask for summaries, extract facts, compare sections, and explore your uploaded material conversationally.</p>
            </div>
            <div class="panel-badge">Grounded Answers</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    chat_container = st.container()
    with chat_container:
        if not st.session_state.messages:
            st.markdown(
                """
                <div class="chat-empty">
                    <div class="chat-empty-title">Your AI conversation space is ready.</div>
                    <div class="chat-empty-copy">
                        Upload a document, then ask for insights, summaries, action items, technical explanations,
                        or evidence-backed answers derived from your files.
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    st.markdown("</div>", unsafe_allow_html=True)

    if prompt := st.chat_input("Ask a question about your documents..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with chat_container:
            with st.chat_message("user"):
                st.markdown(prompt)

        with st.spinner("Thinking..."):
            payload = {"question": prompt, "k": 5}
            try:
                response = requests.post(f"{BASE_API_URL}/api/ask", json=payload, timeout=60)
                if response.status_code == 200:
                    data = response.json()
                    answer = data.get("answer", "No answer received")
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                    with chat_container:
                        with st.chat_message("assistant"):
                            st.markdown(answer)
                else:
                    error_msg = f"Error: {response.text}"
                    st.session_state.messages.append({"role": "assistant", "content": error_msg})
                    with chat_container:
                        with st.chat_message("assistant"):
                            st.markdown(error_msg)
            except Exception as exc:
                error_msg = f"Error: {exc}"
                st.session_state.messages.append({"role": "assistant", "content": error_msg})
                with chat_container:
                    with st.chat_message("assistant"):
                        st.markdown(error_msg)

        st.rerun()
