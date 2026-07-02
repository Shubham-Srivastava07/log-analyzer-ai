import requests
import json
import os

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://172.17.0.1:11434/api/generate")


def get_ai_analysis(summary):
    prompt = f"""
    You are a senior DevOps Engineer.
    Analyze the following log summary and provide a technical report.
    Return the output in clearly formatted markdown:

    1. Root cause
    2. Possible Reasons
    3. Recommended Commands
    4. Fix Steps

    Summary:
    {summary}
    """

    payload = {
            "model" : "llama3.2:3b",
            "prompt" : prompt,
            "stream" : False
    }

    try: 
        response = requests.post("http://127.0.0.1:11434/api/generate", json=payload)
        response.raise_for_status()
        return response.json().get('response', 'No response from AI, ')
    except Exception as e:
        return f"Error connecting to Ollama: {e}"
