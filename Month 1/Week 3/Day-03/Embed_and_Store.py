from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

model = SentenceTransformer('all-MiniLM-L6-v2')


def embed_and_store(texts: list, metadata_list: list, collection_name: str, client: QdrantClient):
  
    collections = [col.name for col in client.get_collections().collections]
    
    if collection_name not in collections:
        print(f"Creating new Qdrant collection: '{collection_name}'...")
        client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=384, distance=Distance.COSINE)
        )

    print(f"Generating embeddings for {len(texts)} items...")
    embeddings = model.encode(texts)

    points = []
    for index in range(len(texts)):
        text = texts[index]
        embedding_vector = embeddings[index].tolist()
        
        payload = {"text": text}
        if index < len(metadata_list):
            payload.update(metadata_list[index])

        point = PointStruct(
            id=index + 1,
            vector=embedding_vector,
            payload=payload
        )
        points.append(point)

    client.upsert(
        collection_name=collection_name,
        points=points
    )
    print(f" Successfully stored {len(points)} documents into '{collection_name}'!\n")



if __name__ == "__main__":
    qdrant_client = QdrantClient(":memory:")

    sample_texts = [
        "RAG stands for Retrieval-Augmented Generation.",
        "Vector databases store high-dimensional embeddings for fast search.",
        "Qdrant allows filtering search results using metadata payloads."
    ]

    sample_metadata = [
        {"source": "doc1.txt", "author": "Alice"},
        {"source": "doc2.txt", "author": "Bob"},
        {"source": "doc3.txt", "author": "Charlie"}
    ]

    embed_and_store(
        texts=sample_texts,
        metadata_list=sample_metadata,
        collection_name="rag_knowledge_base",
        client=qdrant_client
    )

    query = "What is Retrieval-Augmented Generation?"
    query_vector = model.encode(query).tolist()

    search_result = qdrant_client.query_points(
        collection_name="rag_knowledge_base",
        query=query_vector,
        limit=1
    ).points

    print(" Test Query Verification:")
    print(f"Query: '{query}'")
    print(f"Top Match: \"{search_result[0].payload['text']}\"")
    print(f"Metadata: {search_result[0].payload}")