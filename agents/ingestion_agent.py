# agents/ingestion_agent.py

import os
import uuid
from core.document_parser import parse_document
from core.vector_store import embed_and_store
from core.mcp import MCPMessage

def ingest(file_path):
    raw_text = parse_document(file_path)
    doc_id = os.path.basename(file_path)

    # Store embeddings for this document
    embed_and_store(raw_text, doc_id)

    trace_id = str(uuid.uuid4())

    mcp_msg = MCPMessage(
        sender="IngestionAgent",
        receiver="RetrievalAgent",
        message_type="DOCUMENT_INGESTED",
        trace_id=trace_id,
        payload={
            "document": doc_id
        }
    )

    # ✅ Return the message AND document path for use in retrieval
    return mcp_msg, file_path
