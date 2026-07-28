import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from utils import ask

classification_system_prompt = """
You are a highly accurate customer feedback classifier. 
Your task is to classify incoming customer messages into exactly ONE of the following categories:
- Complaint
- Question
- Compliment

=== RULES ===
1. Respond with only the category name (e.g., 'Complaint', 'Question', or 'Compliment').
2. Do NOT include any introductory phrases, punctuation, or explanations.
"""

# 3. List of 5 distinct test customer messages
sample_messages = [
    "Your checkout page keeps crashing every time I try to click the pay button! Please fix this.",
    "Do you offer free shipping to Canada, or is that only for US customers?",
    "I am absolutely in love with this product! It has completely transformed my workflow. Kudos to the team!",
    "My package arrived today, but when I opened it, the USB power cable was missing.",
    "Is the midnight blue edition going to be restocked anytime before the holidays?"
]

print(" Running Zero-Shot Classification Test...")
print("="*65)

for idx, message in enumerate(sample_messages, 1):
    print(f"\nMessage {idx}: \"{message}\"")
    
    result = ask(
        prompt=message, 
        system=classification_system_prompt, 
        temperature=0.0
    )
    
    classification = result.strip() if result else "Error/None"
    
    print(f" Classification: **{classification}**")
    print("-" * 65)

print("\n Zero-shot classification test successfully completed!")