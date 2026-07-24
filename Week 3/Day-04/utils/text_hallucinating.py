from utils.rag_pipeline import run_rag_pipeline
from wrapper_function import ask


def test_hallucination(query: str, client, collection_name: str = "chunks") -> dict:
    
    print("=" * 80)
    print(f" TESTING HALLUCINATION FOR QUERY: '{query}'")
    print("=" * 80)

    raw_prompt = f"Answer the following question: {query}"
    raw_response = ask(prompt=raw_prompt, temperature=0.7)
    
    print("\n 1. RAW GROQ RESPONSE (Without Context):")
    print("-" * 50)
    print(raw_response)

    rag_response = run_rag_pipeline(query=query, client=client, collection_name=collection_name)
    
    print("\n 2. RAG PIPELINE RESPONSE (With Grounded Context):")
    print("-" * 50)
    print(rag_response)
    
    print("\n" + "=" * 80 + "\n")

    return {
        "raw_response": raw_response,
        "rag_response": rag_response
    }