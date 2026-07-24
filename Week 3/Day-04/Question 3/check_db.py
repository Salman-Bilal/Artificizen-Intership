from pathlib import Path
import sys
from qdrant_client import QdrantClient

# 1. Resolve project root path
CURRENT_FILE = Path(__file__).resolve()
PROJECT_ROOT = CURRENT_FILE.parent.parent
DB_PATH = PROJECT_ROOT / "qdrant_db"

print("=" * 70)
print("🔍 QDRANT DATABASE LOCATION DIAGNOSTIC")
print("=" * 70)
print(f"📍 Script Location:  {CURRENT_FILE}")
print(f"📁 Project Root:      {PROJECT_ROOT}")
print(f"💾 Expected DB Path: {DB_PATH.resolve()}")
print(f"❓ Path Exists?      {DB_PATH.exists()}")
print("=" * 70)

if DB_PATH.exists():
    try:
        # Initialize client pointing to local storage folder
        client = QdrantClient(path=str(DB_PATH))
        collections = client.get_collections().collections
        collection_names = [col.name for col in collections]
        
        print(f"✅ Connection Successful!")
        print(f"📦 Collections Found ({len(collection_names)}): {collection_names}")
        
        if "chunks" in collection_names:
            collection_info = client.get_collection("chunks")
            print(f"🎯 Collection 'chunks' exists! Total points/vectors: {collection_info.points_count}")
        else:
            print("⚠️ Collection 'chunks' WAS NOT FOUND in this local database.")
            print("👉 Run Question 2 main.py first to create and populate the 'chunks' collection!")
    except Exception as e:
        print(f"❌ Error connecting to local Qdrant database: {e}")
else:
    print("❌ DB Folder does not exist yet.")
    print("👉 Please run Question 2 main.py to create the 'qdrant_db' folder and ingest document chunks.")

print("=" * 70)