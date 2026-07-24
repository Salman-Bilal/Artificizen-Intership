import sys
from pathlib import Path

CURRENT_FILE = Path(__file__).resolve()
DAY4_DIR = CURRENT_FILE.parents[1]
sys.path.insert(0, str(DAY4_DIR))

from utils.prompt_building import build_prompt

def main():
    user_query = "What is Retrieval-Augmented Generation and how does it work?"
    
    mock_chunks = [
        {
            "text": "Retrieval-Augmented Generation (RAG) combines information retrieval with large language models.",
            "source": "sample_rag_document.pdf",
            "chunk_index": 0
        },
        {
            "text": "Instead of relying only on internal knowledge, RAG retrieves relevant documents from a vector database such as Qdrant.",
            "source": "sample_rag_document.pdf",
            "chunk_index": 1
        }
    ]

    print("=" * 70)
    print(" TESTING BUILD_PROMPT FUNCTION WITH MOCK DATA")
    print("=" * 70)

   
    formatted_prompt = build_prompt(query=user_query, chunks=mock_chunks)

   
    print("\n Generated Prompt:\n")
    print(formatted_prompt)
    print("\n" + "=" * 70)


if __name__ == "__main__":
    main()    