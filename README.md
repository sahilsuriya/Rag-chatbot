# 🤖 Agentic RAG Chatbot (MCP-based) for Multi-Format Document QA

This project is an agent-based Retrieval-Augmented Generation (RAG) chatbot that answers user queries based on uploaded documents in multiple formats — using a structured **Model Context Protocol (MCP)** for communication between agents.

---

## ✅ Features

- 🧠 Agentic Architecture with **IngestionAgent**, **RetrievalAgent**, and **LLMResponseAgent**
- 📄 Supports document formats: `PDF`, `DOCX`, `PPTX`, `CSV`, `TXT`, and `Markdown`
- 🔍 Semantic search powered by **SentenceTransformers** + **FAISS**
- 🧱 Uses **TinyLlama** (HuggingFace) for local language generation (no OpenAI needed)
- 🧾 Source chunks are shown alongside the generated answer
- 🧠 Message passing via **Model Context Protocol (MCP)** structure
- 📺 Simple Streamlit-based user interface

---

## 📁 Project Structure

```bash
agentic-rag-chatbot/
│
├── app/
│   └── ui.py                        # Streamlit UI entry point
│
├── agents/
│   ├── coordinator_agent.py        # Manages flow between agents
│   ├── ingestion_agent.py          # Parses + embeds documents
│   ├── retrieval_agent.py          # Retrieves top chunks
│   └── llm_response_agent.py       # Calls TinyLlama and returns answer
│
├── core/
│   ├── document_parser.py          # Handles parsing logic (pdf, docx, etc.)
│   ├── vector_store.py             # Handles FAISS + chunk embedding
│   └── mcp.py                      # ModelContextProtocol class
│
├── vector_store/                   # Stores dynamic FAISS indexes and chunk metadata
├── requirements.txt
└── README.md


Clone the Repository
git clone https://github.com/sahilsuriya/Rag-chatbot.git
cd agentic-rag-chatbot

Create and Activate Virtual Environment
# Optional but recommended
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install Dependencies
pip install -r requirements.txt

Run the Chatbot
streamlit run app/ui.py
