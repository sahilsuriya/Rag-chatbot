from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os
import pickle

model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.IndexFlatL2(384)
doc_chunks = []

def embed_and_store(text, doc_name):
    global index, doc_chunks

    chunks = [chunk.strip() for chunk in text.split("\n") if chunk.strip()]
    embeddings = model.encode(chunks)

    index.add(np.array(embeddings).astype("float32"))
    doc_chunks.extend(chunks)

    # Save for retrieval
    with open(f"vector_store/{doc_name}_chunks.pkl", "wb") as f:
        pickle.dump(doc_chunks, f)
    faiss.write_index(index, f"vector_store/{doc_name}_index.faiss")
