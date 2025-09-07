import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Gemini API configuration
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
MODEL_NAME = "models/gemini-1.5-flash"

def call_gemini(prompt: str, max_tokens: int = 150) -> str:
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Example interface if needed elsewhere
def call_openai(prompt: str, max_tokens: int = 150) -> str:
    # Optional placeholder or leave empty if you no longer use it
    raise NotImplementedError("OpenAI is not used. Use Gemini instead.")
