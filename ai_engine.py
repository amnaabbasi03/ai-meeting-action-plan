import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_action_plan(transcript):
    prompt = f"""
You are an AI assistant. Analyze the following meeting transcript and generate:
1. A short summary in 3-5 bullet points
2. A list of key decisions
3. Action items with task, owner, and deadline

Transcript:
\"\"\"
{transcript}
\"\"\"

Return JSON format like:
{{
  "summary": ["point1", "point2"],
  "decisions": ["decision1", "decision2"],
  "action_items": [
    {{"task": "Do something", "owner": "Alice", "deadline": "2025-05-20"}},
    ...
  ]
}}
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        content = response.choices[0].message.content
        result = json.loads(content)
        return result["summary"], result["decisions"], result["action_items"]
    except Exception as e:
        print("Error in OpenAI call or parsing:", e)
        return [], [], []

