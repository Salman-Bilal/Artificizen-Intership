import sys
from pathlib import Path
from qdrant_client import QdrantClient

# Resolve to 'Week 3' folder directory
CURRENT_FILE = Path(__file__).resolve()
WEEK3_DIR = CURRENT_FILE.parents[2]  # Adjust parent depth if needed to reach Week 3
sys.path.append(str(WEEK3_DIR))

import pymupdf4llm
from utils.Text_Chunking import chunk_text
from Day_3.Embed_and_Store import embed_and_store


def prepare_document(file_path: Path, collection_name: str = "chunks", client: QdrantClient = None):
    file_path = Path(file_path)
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    # 💾 Force Qdrant to use Week 3 / qdrant_db folder
    if client is None:
        db_path = WEEK3_DIR / "qdrant_db"
        client = QdrantClient(path=str(db_path))

    # 1. Load document content
    if file_path.suffix.lower() == ".pdf":
        text = pymupdf4llm.to_markdown(str(file_path))
    elif file_path.suffix.lower() == ".txt":
        text = file_path.read_text(encoding="utf-8")
    else:
        raise ValueError(f"Unsupported file format: {file_path.suffix}")

    # 2. Chunk text
    chunks = chunk_text(text)

    # 3. Construct metadata list
    metadata = [
        {
            "source": file_path.name,
            "chunk_index": i
        }
        for i in range(len(chunks))
    ]

    # 4. Embed and store in Qdrant
    embed_and_store(
        client=client,
        texts=chunks,
        metadata_list=metadata,
        collection_name=collection_name
    )
    print(f"✅ Stored {len(chunks)} chunks from '{file_path.name}' into collection '{collection_name}'.")