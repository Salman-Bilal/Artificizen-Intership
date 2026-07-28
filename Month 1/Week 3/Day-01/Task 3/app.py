"""
Task: 3: 3.	Run the same prompt three times at temperature=0 and three times at temperature=1.0. Print all six responses and write a one-line observation about the difference.

"""


import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key= os.environ.get("GROQ_API_KEY")
)

prompt = "Summarise what a transformer model does in 3 sentences."
model_name = "llama-3.1-8b-instant"

def get_summary(temp):
    chat_completions = client.chat.completions.create(
        messages= [
            {
                "role" : "user",
                "content" : prompt  
            }
        ],
        model = model_name,
        temperature = temp,
    )
    return chat_completions.choices[0].message.content

print("=== TEMPERATURE 0.0 (Deterministic) ===")
for i in range(3):
    print(f"\n--- Run {i+1} ---")
    print(get_summary(0.0))


print("=== TEMPERATURE 1.0 (Creative) ===")
for i in range(3):
    print(f"\n--- Run {i+1} ---")
    print(get_summary(1.0))
    
