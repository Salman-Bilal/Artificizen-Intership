import os
import time
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def ask(prompt, system=None, model='llama-3.1-8b-instant', temperature=0.7, max_tokens=512):
    client = Groq(
        api_key = os.environ.get("GROQ_API_KEY")
    )
    messages = []

    if system:
        messages.append({
            "role" : "system",
            "content": system
        })
    messages.append({
        "role" : "user",
        "content": prompt
    })
    try:
        chat_completion = client.chat.completions.create(
            messages = messages,
            model = model,
            temperature = temperature,
            max_tokens = max_tokens
        )

        return chat_completion.choices[0].message.content
    
    except Exception as ex:
        print(f"Error during Groq API call: {ex}")
        return None


def ask_detail(prompt, system=None, model='llama-3.1-8b-instant', temperature=0.7, max_tokens=512):
    
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY")
    )
    messages = []

    if system:
        messages.append({
            "role": "system",
            "content": system
        })

    messages.append({
        "role": "user",
        "content": prompt
    })

    start_time = time.time()

    try:
        chat_completion = client.chat.completions.create(
            messages=messages,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens
        )
        latency = time.time() - start_time

        response_text = chat_completion.choices[0].message.content
        total_tokens = chat_completion.usage.total_tokens

        return {
            "text": response_text,
            "total_tokens": total_tokens,
            "latency": latency
        }
    
    except Exception as ex:
        print(f"Error during Groq API call: {ex}")
        return {
            "text": None,
            "total_tokens": 0,
            "latency": 0.0
        }