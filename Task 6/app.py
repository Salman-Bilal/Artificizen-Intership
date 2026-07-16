import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from utils import ask_detail

user_prompt = "Explain the difference between synchronous and asynchronous programming using a real-world restaurant analogy."

print(" Requesting llama-3.1-8b-instant... ")
response_8b_instant = ask_detail(prompt = user_prompt, model= "llama-3.1-8b-instant")

print(" Requesting llama-3.3-70b-versatile... ")

response_70b_versatile = ask_detail(prompt = user_prompt, model = "llama-3.3-70b-versatile")

print("\n" + "="*60)
print("===== Results of Both Models =====")
print("="*60)

print("Model: llama-3.3-8b-instant")
print(f" Latency : {response_8b_instant['latency']:.2f} seconds")
print(f" Total Tokens: {response_8b_instant['total_tokens']}")
print(f" Response: \n {response_8b_instant[ 'text']}")

print("\n" + "-"*60)

print("Model: llama-3.3-70b-versatile")
print(f" Latency : {response_70b_versatile['latency']:.2f} seconds")
print(f" Total Tokens: {response_70b_versatile['total_tokens']}")
print(f" Response: \n {response_70b_versatile[ 'text']}")