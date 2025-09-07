from app.utils.api_clients import call_openai

class ContentAgent:
    def run(self, doubt: str) -> str:
        prompt = f"Create 3 quiz questions based on this programming topic:\n{doubt}"
        return call_openai(prompt)
