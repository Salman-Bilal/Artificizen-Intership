import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

target_sentence = "A dog is chasing a ball"
other_sentences = [
    "A puppy is running after a toy",          
    "A canine is playing outdoors",            
    "A cat is sleeping on the sofa",           
    "The stock market experienced a crash",     
    "A ball is being chased by a dog"          
]

all_sentences = [target_sentence] + other_sentences

embeddings = model.encode(all_sentences)

def cosine_similarity(vec_a, vec_b):
    dot_product = np.dot(vec_a, vec_b)
    norm_a = np.linalg.norm(vec_a)
    norm_b = np.linalg.norm(vec_b)
    return dot_product / (norm_a * norm_b)

target_embedding = embeddings[0]
results = []

for idx, sentence in enumerate(other_sentences, start=1):
    sim = cosine_similarity(target_embedding, embeddings[idx])
    results.append((sentence, float(sim)))

results.sort(key=lambda x: x[1], reverse=True)

print(f" Target Sentence: '{target_sentence}'\n")
print(" Ranked Similarity Results (Most to Least Similar):")
print("-" * 65)
for rank, (sentence, score) in enumerate(results, start=1):
    print(f"{rank}. Score: {score:.4f} | Sentence: '{sentence}'")
print("-" * 65)