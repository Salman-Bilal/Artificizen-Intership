"""
Task: 1: Sign up at console.groq.com, generate an API key, store it in .env as GROQ_API_KEY, and load it with python-dotenv. Never hardcode it.

"""


import os 
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("GROQ_API_KEY")


if api_key:
    print(f"Success! Loaded GROQ_API_KEY: {api_key[:8]}...")
else:
    print("Error: GROQ_API_KEY not found. Make sure your .env file is configured correctly!")