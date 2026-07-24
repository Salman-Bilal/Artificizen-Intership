from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient

# Load embedding model
EMBED_MODEL_NAME = "all-MiniLM-L6-v2"
embedder = SentenceTransformer(EMBED_MODEL_NAME)


def retrieve(
    query: str,
    collection_name: str = "chunks",
    top_k: int = 3,
    client: QdrantClient = None
) -> list[dict]:
    """
    Embeds the user query and retrieves top-k matching chunks from Qdrant.
    Handles automatic connection checking to prevent connection refusal errors.
    """
    # 1. Initialize client with safety fallback
    if client is None:
        try:
            client = QdrantClient(host="localhost", port=6333)
            # Ping server to verify active connection
            client.get_collections()
        except Exception:
            print("⚠️ Local Qdrant server on port 6333 not reachable. Falling back to memory mode.")
            client = QdrantClient(":memory:")

    # 2. Generate query vector
    query_vector = embedder.encode(query).tolist()

    # 3. Search Qdrant
    if hasattr(client, "query_points"):
        search_results = client.query_points(
            collection_name=collection_name,
            query=query_vector,
            limit=top_k
        ).points
    else:
        search_results = client.search(
            collection_name=collection_name,
            query_vector=query_vector,
            limit=top_k
        )

    # 4. Format payload & scores
    retrieved_chunks = []
    for hit in search_results:
        retrieved_chunks.append({
            "text": hit.payload.get("text") or hit.payload.get("page_content", ""),
            "source": hit.payload.get("source"),
            "chunk_index": hit.payload.get("chunk_index"),
            "score": round(hit.score, 4)
        })

    return retrieved_chunks