import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from utils import ask

puzzle = "If it takes 5 machines 5 minutes to make 5 widgets, how long would it take 100 machines to make 100 widgets?"

print(" STARTING LOGIC PUZZLE BENCHMARK ")
print("="*65)


print("\n Run 1: Requesting response WITHOUT Chain-of-Thought...")
response_no_cot = ask(prompt=puzzle, temperature=0.0)

print("\n--- Output WITHOUT CoT ---")
print(response_no_cot)
print("-" * 65)



print("\n Run 2: Requesting response WITH Chain-of-Thought...")
cot_prompt = puzzle + "\nThink step by step before providing the final answer."
response_with_cot = ask(prompt=cot_prompt, temperature=0.0)

print("\n--- Output WITH CoT ---")
print(response_with_cot)
print("="*65)