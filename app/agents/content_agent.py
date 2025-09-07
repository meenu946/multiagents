from app.utils.api_clients import call_gemini

class ContentAgent:
    def run(self, doubt: str) -> str:
        prompt = f"Generate quiz questions based on the topic: {doubt}"
        return call_gemini(prompt)
