from utils.retriever import retrieve
from utils.prompt_building import build_prompt
from wrapper_function import ask


def run_rag_pipeline(query: str, client, collection_name: str = "chunks") -> str:
    """
    End-to-end RAG pipeline:
    1. Retrieve relevant text chunks from Qdrant vector database.
    2. Build a grounded prompt with strict context rules.
    3. Query the Groq LLM using wrapper_function.ask.
    """
    # Step 1: Retrieve matching chunks
    chunks = retrieve(
        query=query,
        collection_name=collection_name,
        top_k=3,
        client=client
    )
    
    # Step 2: Build grounded prompt
    prompt = build_prompt(query=query, chunks=chunks)
    
    # Step 3: Send prompt to Groq API (temperature=0.0 for deterministic answers)
    response = ask(prompt=prompt, temperature=0.0)
    
    return response