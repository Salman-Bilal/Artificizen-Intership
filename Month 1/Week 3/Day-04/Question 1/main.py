
import sys
from pathlib import Path

import sys
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from utils.Text_Chunking import chunk_text


sample_sentence = "Artificial intelligence and retrieval augmented generation are transforming enterprise systems. "
mock_3000_word_doc = sample_sentence * 300
    
word_count = len(mock_3000_word_doc.split())
char_count = len(mock_3000_word_doc)
    
print(f"📄 Document Word Count: {word_count:,} words")
print(f"🔤 Document Character Count: {char_count:,} characters\n")

chunks = chunk_text(mock_3000_word_doc, chunk_size=500, overlap=50)

    
print(f"🧩 Total Chunks Produced: {len(chunks)}")

print("\n--- 🔍 Chunk Overlap Verification ---")
print(f"Chunk 1 (End):   ...{repr(chunks[0][-60:])}")
print(f"Chunk 2 (Start): {repr(chunks[1][:60])}...")