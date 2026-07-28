import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from utils import ask

meeting_transcript = """
Project Orion Status Meeting - July 17, 2026
Sarah: "We absolutely need to update the API documentation by this Wednesday. Customers are complaining about outdated endpoint specifications."
John: "I will tackle the critical database migration tonight. It needs to happen before the deployment."
Alex: "I can look into designing the new landing page UI, but I probably won't get to it until late next week since it's not super urgent."
Sarah: "Perfect. Also, John, please make sure to order more backup servers by Friday just in case our traffic spikes during launch."
"""

print(" STARTING THREE-STEP PROMPT CHAIN PIPELINE ")
print("=" * 70)
print(f" Raw Transcript Input:\n{meeting_transcript.strip()}")
print("=" * 70)


print("\n [Step 1/3] Extracting action items from transcript...")
step1_prompt = f"""
Identify and list all distinct action items, tasks, or assignments mentioned in the following transcript. 
Identify who is assigned to each task and any mentioned deadline.

Transcript:
{meeting_transcript}
"""

step1_output = ask(prompt=step1_prompt, temperature=0.1)

if not step1_output:
    print(" Step 1 failed to return an output.")
    sys.exit(1)

print("\n--- Output Step 1 (Raw Action Items) ---")
print(step1_output.strip())
print("-" * 70)



print("\n [Step 2/3] Assigning priorities (High / Medium / Low)...")
step2_prompt = f"""
For each action item listed below, analyze its urgency and assign a priority level: High, Medium, or Low.
Explain briefly in one sentence why you assigned that priority level.

Action Items:
{step1_output}
"""

step2_output = ask(prompt=step2_prompt, temperature=0.2)

if not step2_output:
    print(" Step 2 failed to return an output.")
    sys.exit(1)

print("\n--- Output Step 2 (Prioritized Action Items) ---")
print(step2_output.strip())
print("-" * 70)


print("\n [Step 3/3] Formatting output as a JSON array...")
step3_system = "You are a strict JSON generator. You only output raw, valid JSON arrays. Do not apologize, explain, or use markdown formatting."
step3_prompt = f"""
Convert the prioritized action items list below into a single valid JSON array of objects.
Each object must have exactly these keys: "task", "assignee", "deadline", "priority", and "reasoning".

If a deadline or assignee is not specified, set its value to null.

Prioritized Action Items:
{step2_output}
"""

step3_output = ask(prompt=step3_prompt, system=step3_system, temperature=0.0)

print("\n--- Final Output Step 3 (Strict JSON Array) ---")
if step3_output:
    print(step3_output.strip())
else:
    print(" Step 3 failed to return an output.")
print("=" * 70)
print(" PIPELINE EXECUTION COMPLETE ")