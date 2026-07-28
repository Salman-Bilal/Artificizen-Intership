import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def semantic_search(query: str, documents: list[str], top_k: int = 3) -> list[tuple[str, float]]:
    if not documents:
        return []

    query_embedding = model.encode(query)
    doc_embeddings = model.encode(documents)

    dot_products = np.dot(doc_embeddings, query_embedding)
    query_norm = np.linalg.norm(query_embedding)
    doc_norms = np.linalg.norm(doc_embeddings, axis=1)
    
    similarity_scores = dot_products / (doc_norms * query_norm + 1e-10)

    results = list(zip(documents, similarity_scores))

    results.sort(key=lambda x: x[1], reverse=True)

    return [(doc, float(score)) for doc, score in results[:top_k]]


if __name__ == "__main__":
    search_query = "What causes rain and precipitation?"
    
    corpus = [
        "Water vapor condenses in atmosphere to form clouds and falls as rain.",
        "The financial stock market closed higher after quarterly earnings reports.",
        "Golden retrievers are friendly dogs that make great family pets.",
        "Precipitation happens when droplets in clouds become too heavy to remain suspended.",
        "Solar panels convert sunlight directly into electric current.",
        "Monsoon winds bring heavy rainfall and storm systems across the region."
    ]

    top_matches = semantic_search(search_query, corpus, top_k=3)

    print(f"Search Query: '{search_query}'\n")
    print("Top 3 Semantic Search Results:")
    print("-" * 70)
    for rank, (doc, score) in enumerate(top_matches, start=1):
        print(f"Rank {rank} | Score: {score:.4f} | Document: '{doc}'")
    print("-" * 70)