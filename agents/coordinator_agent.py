# agents/coordinator_agent.py

import uuid
from agents import ingestion_agent, retrieval_agent, llm_response_agent
from core.mcp import MCPMessage

class CoordinatorAgent:
    def __init__(self):
        self.trace_log = {}
        self.current_doc_name = None

    def ingest_document(self, file_path):
        mcp_msg, _ = ingestion_agent.ingest(file_path)  # ✅ unpack tuple correctly
        trace_id = mcp_msg.trace_id
        self.current_doc_name = mcp_msg.payload["document"]
        self.trace_log[trace_id] = [mcp_msg]
        return trace_id, mcp_msg

    def handle_query(self, query):
        trace_id = str(uuid.uuid4())
        if not self.current_doc_name:
            raise ValueError("No document ingested yet.")

        retrieval_msg = retrieval_agent.retrieve(query, self.current_doc_name)
        self.trace_log[trace_id] = [retrieval_msg]

        llm_response = llm_response_agent.generate_response(retrieval_msg)

        return {
            "trace_id": trace_id,
            "mcp_messages": self.trace_log[trace_id],
            "answer": llm_response['answer'],
            "sources": llm_response['sources']
        }
