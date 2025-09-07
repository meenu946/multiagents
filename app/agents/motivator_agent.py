import random

class MotivatorAgent:
    def run(self) -> str:
        messages = [
            "🚀 Keep going, you’re doing amazing!",
            "💡 Every doubt you solve makes you stronger.",
            "🔥 Great effort! You’re one step closer to mastery.",
        ]
        return random.choice(messages)
