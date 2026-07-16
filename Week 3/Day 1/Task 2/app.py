"""
Task: 2: Call the Groq API using llama-3.1-8b-instant and print a completion for: “Summarise what a transformer model does in 3 sentences.”

"""


import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key= os.environ.get("GROQ_API_KEY")
)

chat_completion = client.chat.completions.create(
    messages = [
        {

            "role" : "user",
            "content" : "Summarise what a transformer model does in 3 sentences."
        }
    ],
    model= "llama-3.1-8b-instant",
)

print(chat_completion.choices[0].message.content)