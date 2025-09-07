from app.utils.api_clients import call_openai

class TeacherAgent:
    def run(self, doubt: str) -> str:
        prompt = f"Explain the following coding doubt in simple terms for a beginner:\n{doubt}"
        return call_openai(prompt)
