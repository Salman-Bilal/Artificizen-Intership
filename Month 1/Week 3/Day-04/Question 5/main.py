import sys
from pathlib import Path

CURRENT_FILE = Path(__file__).resolve()
DAY4_DIR = CURRENT_FILE.parents[1]   
WEEK3_DIR = CURRENT_FILE.parents[2]  

sys.path.insert(0, str(DAY4_DIR))
sys.path.append(str(WEEK3_DIR))

from qdrant_client import QdrantClient
from utils.rag_pipeline import run_rag_pipeline


def main():
    db_path = WEEK3_DIR / "qdrant_db"
    print(f" Connecting to Qdrant DB at: {db_path.resolve()}\n")

    client = QdrantClient(path=str(db_path))
    collection_name = "chunks"

    test_questions = [
        "What is Retrieval-Augmented Generation and how does it work?",
        "Which vector database is mentioned for storing embeddings?",
        "What is the capital city of France?"  # Expected fallback: "I don't know."
    ]

    print("=" * 75)
    print(" QUESTION 5: END-TO-END RAG PIPELINE EVALUATION")
    print("=" * 75)

    for idx, question in enumerate(test_questions, start=1):
        print(f"\n Question [{idx}]: {question}")
        print("-" * 75)
        
        answer = run_rag_pipeline(query=question, client=client, collection_name=collection_name)
        
        print(f" LLM Response:\n{answer}")
        print("=" * 75)

    client.close()


if __name__ == "__main__":
    main()