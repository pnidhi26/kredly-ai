import chromadb

from app.chunking import sentence_split
from .embeddings import get_embedding_model

# New Chroma client (NO legacy Settings)
client = chromadb.Client()

# Create or get collection
collection = client.get_or_create_collection(
    name="documents"
)

def reset_store():
    global collection

    try:
        client.delete_collection("documents")
    except Exception:
        # Collection may not exist yet
        pass

    collection = client.get_or_create_collection("documents")


def add_chunks(chunks, file_name):
    model = get_embedding_model()

    documents = []
    metadatas = []
    ids = []

    for idx, chunk in enumerate(chunks):
        sentences = sentence_split(chunk)
        embeddings = model.encode(sentences).tolist()

        for i, sent in enumerate(sentences):
            documents.append(sent)
            metadatas.append({
                "file": file_name,
                "type": "sentence"
            })
            ids.append(f"{file_name}_{idx}_{i}")

    collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )

def search(query, k=5):
    model = get_embedding_model()
    q_embedding = model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=q_embedding,
        n_results=k
    )

    docs = results["documents"][0]
    distances = results["distances"][0]
    metadatas = results["metadatas"][0]

    return docs, distances, metadatas



