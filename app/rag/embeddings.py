from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

from data.knowledge_base import knowledge_base

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Convert KB incidents into documents
documents = [item["incident"] for item in knowledge_base]

# Generate embeddings
embeddings = model.encode(documents)

# Convert to numpy float32
embeddings = np.array(embeddings).astype("float32")

# Create FAISS index
dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

# Add embeddings
index.add(embeddings)


def retrieve_similar_incidents(query, top_k=2):

    # Convert query into embedding
    query_embedding = model.encode([query])

    query_embedding = np.array(query_embedding).astype("float32")

    # Search FAISS
    distances, indices = index.search(query_embedding, top_k)

    results = []

    for idx in indices[0]:
        results.append(documents[idx])

    return results