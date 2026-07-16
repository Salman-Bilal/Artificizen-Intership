"""
Task: 4: Write a wrapper function ask(prompt, system=None, model='llama-3.1-8b-instant', temperature=0.7, max_tokens=512) that calls Groq and returns only the text string. This function will be reused every day this week.

-> wrapper function "ask" is created in the main Week 3 folder 

"""


import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from utils import ask

response = ask("Give me a one-sentence motivation for a software intern.")
print(f"Response of wrapper function Ask : {response}")