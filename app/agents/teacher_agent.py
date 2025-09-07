from app.utils.api_clients import call_gemini

class TeacherAgent:
    def run(self, doubt: str) -> str:
        prompt = f"Explain this coding doubt clearly: {doubt}"
        return call_gemini(prompt)
