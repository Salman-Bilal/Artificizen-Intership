import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = [
    "Solar panels turn sunlight into electricity.",
    "Fresh coffee has a strong and nice smell.",
    "The stock market went up today.",
    "Dolphins talk to each other using clicks.",
    "Monsoon season brings a lot of rain.",
    "Baking bread requires flour and yeast.",
    "The Renaissance was an important time in history.",
    "Electric cars run on big batteries.",
    "Mount Everest is the tallest mountain.",
    "Mozart wrote beautiful classical music.",
    "Drinking enough water is good for health.",
    "Quantum computers can solve hard problems fast.",
    "Volcanoes throw out hot lava when they erupt.",
    "The Eiffel Tower is located in Paris.",
    "The brown dog ran fast in the yard chasing a ball.", 
    "Bees help plants grow by pollinating flowers.",
    "Virtual reality lets you play games in 3D.",
    "The Great Wall of China is very long.",
    "Plants use sunlight to make food.",
    "Warm tea helps people sleep better.",
    "Good passwords keep your account safe.",
    "Coral reefs are home to many ocean creatures.",
    "AI can read data and find patterns.",
    "The Amazon river is inside a huge rainforest.",
    "Scuba divers like to look at old shipwrecks.",
    "Airplane wings are made to cut through air.",
    "The Mona Lisa is a famous painting.",
    "Storms can cause strong winds and tornadoes.",
    "Some fish live deep down in the dark ocean.",
    "Learning new languages is good for your brain.",
    "Space telescopes take pictures of far stars.",
    "Running every day makes your heart stronger.",
    "An orchestra has many musical instruments.",
    "Ice sheets are melting due to warm weather.",
    "Tiny bacteria live in soil everywhere.",
    "Chess is a game that needs good planning.",
    "The Grand Canyon has deep rock layers.",
    "GPS uses satellites to find your location.",
    "Organic vegetables are grown without pesticides.",
    "Human brains have billions of cells.",
    "Architects draw plans to build big houses.",
    "Burning coal produces dirty air.",
    "Yoga helps stretch your body muscles.",
    "Pyramids were built in ancient Egypt.",
    "Self-driving cars use cameras to navigate.",
    "The space station goes around the Earth.",
    "Marathon runners train for a long time.",
    "The Sahara is a very hot and dry desert.",
    "Artists use bright paint colors on canvas.",
    "Milk is turned into cheese using bacteria."
]

print("Embedding 50 sentences...")
sentence_embeddings = model.encode(sentences)

query = "A canine sprinted rapidly through the garden following a felt sphere."

print(f"\nSearch Query: '{query}'")

query_embedding = model.encode(query)

def calculate_similarity(vector_a, vector_b):
    dot_product = np.dot(vector_a, vector_b)
    norm_a = np.linalg.norm(vector_a)
    norm_b = np.linalg.norm(vector_b)
    return dot_product / (norm_a * norm_b)

scores_list = []

for index in range(len(sentences)):
    current_sentence = sentences[index]
    current_embedding = sentence_embeddings[index]
    
    score = calculate_similarity(query_embedding, current_embedding)
    
    scores_list.append((index, current_sentence, score))

scores_list.sort(key=lambda item: item[2], reverse=True)

print("\n Top 3 Semantic Search Matches:")
print("=" * 65)

for rank in range(3):
    item = scores_list[rank]
    sentence_index = item[0]
    matched_text = item[1]
    similarity_score = item[2]
    
    print(f"Rank {rank + 1} | Score: {similarity_score:.4f} | Index: {sentence_index}")
    print(f"Text: \"{matched_text}\"")
    print("-" * 65)

top_match_index = scores_list[0][0]

if top_match_index == 14:
    print("\n Verification Successful: Semantic search found the correct match even though different words were used!")
else:
    print("\n Verification Failed: The top result was not the expected sentence.")