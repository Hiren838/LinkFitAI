import requests

def generate_message(candidate, job_title, company):
    API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-2-7b-chat-hf"
    headers = {"Authorization": f"Bearer TOKEN"}

    prompt = f"""
You are a recruiter. Here's the candidate:
Title: {candidate['title']}
Snippet: {candidate['snippet']}

You are hiring for a {job_title} role at {company}.
Write a short personalized outreach message referencing the candidate's experience.
"""

    payload = {
        "inputs": prompt,
        "parameters": {
            "temperature": 0.7,
            "max_new_tokens": 200
        }
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        generated = response.json()
        # Check response structure (list of dicts with 'generated_text')
        try:
            return generated[0]['generated_text']
        except:
            return str(generated)
    else:
        return f"Message generation failed: {response.status_code} {response.text}"
