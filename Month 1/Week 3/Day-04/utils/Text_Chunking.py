def chunk_text(text: str, chunk_size: int = 400, overlap: int = 50) -> list[str]:
    
    words = text.split()
    chunks = []
    
    current_chunk = []
    current_length = 0
    
    for word in words:
        current_chunk.append(word)
        current_length += len(word) + 1  # Add 1 for the space
        
        if current_length >= chunk_size:
            chunks.append(" ".join(current_chunk))
            # Maintain overlap for semantic continuity
            overlap_words = current_chunk[-max(1, overlap // 6):]
            current_chunk = overlap_words
            current_length = sum(len(w) + 1 for w in current_chunk)
            
    if current_chunk:
        chunks.append(" ".join(current_chunk))
        
    return chunks