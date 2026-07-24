# Load a plain-text or PDF file, chunk it, embed all chunks with sentence-transformers,
# and store them in Qdrant with source filename and chunk index as metadata.

from pathlib import Path
import sys

# Resolve base directory path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from utils.load_documents import prepare_document

if __name__ == "__main__":
    # Specify target document path (PDF or TXT)
    doc_path = Path(__file__).resolve().parents[1] / "sample_rag_document.pdf"
    
    # Run the end-to-end loading, chunking, and Qdrant ingestion pipeline
    prepare_document(doc_path)