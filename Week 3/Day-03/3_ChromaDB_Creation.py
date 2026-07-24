import chromadb

client = chromadb.Client()


collection = client.create_collection(name="space_knowledge_base")


paragraphs = [
    "The Sun is the star at the center of the Solar System. It is a nearly perfect ball of hot plasma.",
    "Mars is the fourth planet from the Sun and the second-smallest planet in the Solar System.",
    "A black hole is a region of spacetime where gravity is so strong that nothing can escape from it.",
    "The James Webb Space Telescope provides unprecedented resolution for observing distant celestial objects.",
    "Jupiter is the largest planet in our solar system and is known for its iconic Great Red Spot storm.",
    "Neutron stars are the collapsed cores of massive supergiant stars, possessing immense density.",
    "The Milky Way is a barred spiral galaxy that contains hundreds of billions of stars including our Sun.",
    "Comets are icy small Solar System bodies that warm up and release gases when passing close to the Sun.",
    "Exoplanets are planets that orbit stars outside our own solar system in distant galaxies.",
    "Saturn is famous for its extensive ring system made mostly of ice particles, rocky debris, and dust."
]

ids = [f"doc_{i+1}" for i in range(len(paragraphs))]

collection.add(
    documents=paragraphs,
    ids=ids
)

print(f" Successfully inserted {collection.count()} documents into in-memory ChromaDB!\n")

query = "Which space telescope or instrument takes high-resolution images of deep space?"

print(f" Natural Language Query: '{query}'\n")

results = collection.query(
    query_texts=[query],
    n_results=2
)

print(" Top 2 Most Relevant Results:")
print("=" * 70)

for i in range(len(results['documents'][0])):
    doc_id = results['ids'][0][i]
    document = results['documents'][0][i]
    distance = results['distances'][0][i] 
    
    print(f"Rank {i+1} [ID: {doc_id}] (Distance Score: {distance:.4f})")
    print(f" Paragraph: \"{document}\"")
    print("-" * 70)
