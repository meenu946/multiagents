class DebuggerAgent:
    def run(self, code: str) -> str:
        if not code:
            return "🐞 Debugger: No code provided."
        return "🐞 Debugger: I analyzed your code and suggest this fix..."
