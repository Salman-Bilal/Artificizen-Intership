def build_prompt(query: str, chunks: list[dict]) -> str:
    context_str = ""
    
    for idx, chunk in enumerate(chunks, start=1):
        text = chunk.get("text") or chunk.get("page_content") or str(chunk)
        context_str += f"Context Item [{idx}]:\n{text.strip()}\n\n"
        
    prompt = f"""Use the following pieces of retrieved context to answer the user's question.

--- CONTEXT START ---
{context_str.strip()}
--- CONTEXT END ---

User Question: {query}

Answer using only the context above. If the answer is not in the context, say: I don't know."""

    return prompt