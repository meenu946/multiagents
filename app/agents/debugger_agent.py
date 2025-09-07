from app.utils.api_clients import call_openai

class DebuggerAgent:
    def run(self, code: str) -> str:
        if not code.strip():
            return "🐞 Debugger: No code provided."
        prompt = f"Debug the following Python code and suggest improvements or fixes:\n{code}"
        return call_openai(prompt)
