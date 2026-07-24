from pathlib import Path
import sys

# Resolve path directly to 'Week 3' folder
CURRENT_FILE = Path(__file__).resolve()
DAY4_DIR = CURRENT_FILE.parents[1]   # Points to 'Day 4'
WEEK3_DIR = CURRENT_FILE.parents[2]  # Points to 'Week 3'

# 1. Add DAY4_DIR first so 'from utils.retriever' loads 'Day 4/utils/retriever.py'
sys.path.insert(0, str(DAY4_DIR))
sys.path.append(str(WEEK3_DIR))

from qdrant_client import QdrantClient
from utils.retriever import retrieve

def main():
    # Explicit path to Week 3/qdrant_db
    db_path = WEEK3_DIR / "qdrant_db"
    print(f"📁 Connecting to Qdrant DB at: {db_path.resolve()}")

    client = QdrantClient(path=str(db_path))
    
    collection_name = "chunks"
    user_query = "What is Retrieval-Augmented Generation and how does it work?"

    print("=" * 65)
    print(f"🔍 SEARCH QUERY: '{user_query}'")
    print("=" * 65)

    results = retrieve(
        query=user_query,
        collection_name=collection_name,
        top_k=3,
        client=client
    )

    print(f"✨ Top {len(results)} Retrieved Chunks:\n")
    for idx, item in enumerate(results, start=1):
        print(f"[{idx}] Similarity Score: {item['score']}")
        print(f"    Source File:      {item['source']}")
        print(f"    Chunk Index:      {item['chunk_index']}")
        print(f"    Content Preview:  {item['text'][:150]}...")
        print("-" * 65)

    # Clean explicit close to suppress msvcrt warning
    client.close()

if __name__ == "__main__":
    main()