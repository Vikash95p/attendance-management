import os
import json
from google import genai


api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY is not set.")


client = genai.Client(api_key=api_key)


def inference_client(request, attendance_data):

    prompt = f"""
You are an AI attendance assistant.

Attendance data:
{json.dumps(attendance_data, indent=2)}

User request:
{json.dumps(request, indent=2)}

Perform the requested attendance operation.

Return ONLY valid JSON.
Do not return markdown.
Do not return explanations.

For check_attendance, return:
{{
    "action": "check_attendance",
    "roll_no": "...",
    "date": "...",
    "present": true or false
}}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return json.loads(response.text)