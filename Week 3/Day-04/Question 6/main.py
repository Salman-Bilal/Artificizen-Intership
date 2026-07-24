import sys
from pathlib import Path

CURRENT_FILE = Path(__file__).resolve()
DAY4_DIR = CURRENT_FILE.parents[1]   
WEEK3_DIR = CURRENT_FILE.parents[2]  

sys.path.insert(0, str(DAY4_DIR))
sys.path.append(str(WEEK3_DIR))

from qdrant_client import QdrantClient
from utils.text_hallucinating import test_hallucination


def main():
    db_path = WEEK3_DIR / "qdrant_db"
    print(f" Connecting to Qdrant DB at: {db_path.resolve()}\n")

    client = QdrantClient(path=str(db_path))
    collection_name = "chunks"

    in_context_query = "Which vector database is specified in the document for storing embeddings?"
    test_hallucination(query=in_context_query, client=client, collection_name=collection_name)

    out_of_context_query = "What is the capital city of France?"
    test_hallucination(query=out_of_context_query, client=client, collection_name=collection_name)

    client.close()


if __name__ == "__main__":
    main()