from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct, Filter, FieldCondition, MatchValue
from sentence_transformers import SentenceTransformer

client = QdrantClient(":memory:")

model = SentenceTransformer('all-MiniLM-L6-v2')
vector_size = model.get_sentence_embedding_dimension()  # 384 dimensions for all-MiniLM-L6-v2

collection_name = "space_knowledge_base"
client.create_collection(
    collection_name=collection_name,
    vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE)
)

documents_data = [
    {
        "text": "The Sun is the star at the center of the Solar System. It is a nearly perfect ball of hot plasma.",
        "source": "web"
    },
    {
        "text": "Mars is the fourth planet from the Sun and the second-smallest planet in the Solar System.",
        "source": "manual"
    },
    {
        "text": "A black hole is a region of spacetime where gravity is so strong that nothing can escape from it.",
        "source": "web"
    },
    {
        "text": "The James Webb Space Telescope provides unprecedented resolution for observing distant celestial objects.",
        "source": "manual"
    },
    {
        "text": "Jupiter is the largest planet in our solar system and is known for its iconic Great Red Spot storm.",
        "source": "web"
    },
    {
        "text": "Neutron stars are the collapsed cores of massive supergiant stars, possessing immense density.",
        "source": "manual"
    },
    {
        "text": "The Milky Way is a barred spiral galaxy that contains hundreds of billions of stars including our Sun.",
        "source": "web"
    },
    {
        "text": "Comets are icy small Solar System bodies that warm up and release gases when passing close to the Sun.",
        "source": "manual"
    },
    {
        "text": "Exoplanets are planets that orbit stars outside our own solar system in distant galaxies.",
        "source": "web"
    },
    {
        "text": "Saturn is famous for its extensive ring system made mostly of ice particles, rocky debris, and dust.",
        "source": "manual"
    }
]

texts = [doc["text"] for doc in documents_data]
embeddings = model.encode(texts)

points = [
    PointStruct(
        id=idx + 1,
        vector=embeddings[idx].tolist(),
        payload={
            "text": doc["text"],
            "source": doc["source"]
        }
    )
    for idx, doc in enumerate(documents_data)
]

client.upsert(
    collection_name=collection_name,
    points=points
)

print(f" Successfully inserted {len(points)} documents into in-memory Qdrant!\n")

query = "Which space telescope or instrument takes high-resolution images of deep space?"
query_vector = model.encode(query).tolist()

print(f" Query: '{query}'")
print(" Filter condition: source == 'manual'\n")

manual_filter = Filter(
    must=[
        FieldCondition(
            key="source",
            match=MatchValue(value="manual")
        )
    ]
)

search_results = client.query_points(
    collection_name=collection_name,
    query=query_vector,
    query_filter=manual_filter,
    limit=2
).points

print(" Top 2 Most Relevant Results (Filtered by source == 'manual'):")
print("=" * 70)

for rank, hit in enumerate(search_results, start=1):
    doc_text = hit.payload["text"]
    source = hit.payload["source"]
    score = hit.score  # Cosine similarity score (higher is better)
    
    print(f"Rank {rank} [ID: {hit.id}] (Score: {score:.4f}) | Source: '{source}'")
    print(f" Paragraph: \"{doc_text}\"")
    print("-" * 70)