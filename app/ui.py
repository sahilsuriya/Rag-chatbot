import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import os
import streamlit as st
from agents.coordinator_agent import CoordinatorAgent

# Initialize CoordinatorAgent
coordinator = CoordinatorAgent()

# Set page config
st.set_page_config(page_title="📄 Agentic RAG Chatbot", layout="wide")

# App Title
st.title("📄 Agentic RAG Chatbot with MCP & Multi-Format Support")

# File uploader section
uploaded_files = st.file_uploader(
    "📤 Upload Documents (PDF, DOCX, PPTX, CSV, TXT, Markdown)",
    type=["pdf", "docx", "pptx", "csv", "txt", "md"],
    accept_multiple_files=True
)

# Document ingestion
if uploaded_files:
    st.subheader("📚 Document Ingestion")
    for file in uploaded_files:
        file_path = os.path.join("uploaded_docs", file.name)
        os.makedirs("uploaded_docs", exist_ok=True)
        with open(file_path, "wb") as f:
            f.write(file.read())
        trace_id, mcp = coordinator.ingest_document(file_path)
        st.success(f"Ingested: {file.name} (Trace ID: {trace_id})")

# Ask a question
st.subheader("💬 Ask a Question Based on Uploaded Docs")
query = st.text_input("What would you like to know?")

# Answer generation
if query:
    with st.spinner("🔍 Retrieving context and generating response..."):
        response = coordinator.handle_query(query)
        st.markdown("### 🤖 Answer")
        st.write(response["answer"])

        st.markdown("### 📄 Source Chunks")
        for i, chunk in enumerate(response["sources"], start=1):
            st.markdown(f"**Chunk {i}:**\n> {chunk}")
