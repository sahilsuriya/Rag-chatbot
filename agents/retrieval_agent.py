# agents/retrieval_agent.py

import uuid
from core.mcp import MCPMessage
from core.vector_store import search

def retrieve(query, doc_name):
    top_chunks = search(query, doc_name)  # Use actual semantic search

    trace_id = str(uuid.uuid4())
    mcp_msg = MCPMessage(
        sender="RetrievalAgent",
        receiver="LLMResponseAgent",
        message_type="RETRIEVAL_RESULT",
        trace_id=trace_id,
        payload={
            "top_chunks": top_chunks,
            "query": query
        }
    )
    return mcp_msg
