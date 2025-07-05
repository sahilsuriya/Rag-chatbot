# core/vector_store.py

import os
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

# Load embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")

# Ensure vector_store directory exists
os.makedirs("vector_store", exist_ok=True)

def embed_and_store(text, doc_name):
    # Split text into cleaned chunks
    chunks = [chunk.strip() for chunk in text.split("\n") if chunk.strip()]
    if not chunks:
        raise ValueError("No valid text chunks to embed.")

    embeddings = model.encode(chunks)

    # Create FAISS index and add vectors
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings).astype("float32"))

    # Save chunks and index
    faiss.write_index(index, f"vector_store/{doc_name}_index.faiss")
    with open(f"vector_store/{doc_name}_chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)

def search(query, doc_name, k=3):
    index_path = f"vector_store/{doc_name}_index.faiss"
    chunks_path = f"vector_store/{doc_name}_chunks.pkl"

    # Check for existence
    if not os.path.exists(index_path) or not os.path.exists(chunks_path):
        raise FileNotFoundError(f"Vector store files for {doc_name} not found.")

    # Load index and chunks
    index = faiss.read_index(index_path)
    with open(chunks_path, "rb") as f:
        chunks = pickle.load(f)

    # Get query embedding
    query_vec = model.encode([query])
    D, I = index.search(np.array(query_vec).astype("float32"), k)

    # Return top matching chunks
    return [chunks[i] for i in I[0] if i < len(chunks)]
