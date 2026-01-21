import chromadb
from chromadb.utils import embedding_functions

client = chromadb.Client()
collection = client.get_or_create_collection(
    name="kredly_docs",
    embedding_function=embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
)

def add_chunks(chunks, file_name):
    for i, chunk in enumerate(chunks):
        collection.add(
            documents=[chunk],
            metadatas=[{"file": file_name}],
            ids=[f"{file_name}_{i}"]
        )


def search(query, k=5):
    results = collection.query(
        query_texts=[query],
        n_results=k
    )

    docs = results["documents"][0]
    distances = results["distances"][0]
    metas = results["metadatas"][0]

    return docs, distances, metas
