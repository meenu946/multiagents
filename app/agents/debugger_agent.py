from app.utils.api_clients import call_gemini

class DebuggerAgent:
    def run(self, code: str) -> str:
        prompt = f"Find bugs and improvements in this Python code:\n{code}"
        return call_gemini(prompt)
