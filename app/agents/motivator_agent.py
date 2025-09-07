from app.utils.api_clients import call_gemini

class MotivatorAgent:
    def run(self) -> str:
        prompt = "Provide a motivational message for a learner facing difficulties."
        return call_gemini(prompt)
