"""
Task: 5: Pass a system message: “You are a strict JSON-only responder. Never output anything outside a JSON object.” Ask any question and print the raw output. Did it obey?

"""


import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from utils import ask

system_prompt = "You are a strict JSON-only responder. Never output anything outside a JSON object."
prompt = "What are the top three most popular programming languages in 2026?"

print("======= Sending Request to Groq =======")

response = ask(prompt, system_prompt)

print("====== OUTPUT =======")
print(response)