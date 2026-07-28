import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from utils import ask

buggy_code = """
def add_user_to_list(username, user_list=[]):
    try:
        user_list.append(username)
        print("Successfully added " + username)
        return user_list
    except:
        pass
"""

print(" RUNNING CODE REVIEWER ")
print("="*65)


print("\n Run 1: Reviewing code with DEFAULT system prompt...")
response_default = ask(
    prompt=f"Please review this Python code and suggest improvements:\n{buggy_code}", 
    temperature=0.2
)

print("\n--- Output with DEFAULT System Prompt ---")
print(response_default)
print("-" * 65)



print("\n Run 2: Reviewing code with STRICT SENIOR REVIEWER system prompt...")
strict_reviewer_system = (
    "You are a strict, senior Python code reviewer. Your feedback must be highly concise, "
    "actionable, and straight to the point. Provide absolutely no praise, introductory greetings, "
    "or conversational fluff (e.g., do not say 'Here is my review'). Only output a bulleted list "
    "of critical issues and their direct code fixes."
)

response_strict = ask(
    prompt=f"Please review this Python code:\n{buggy_code}", 
    system=strict_reviewer_system, 
    temperature=0.0  
)

print("\n--- Output with STRICT SENIOR REVIEWER System Prompt ---")
print(response_strict)
print("="*65)