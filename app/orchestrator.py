from app.agents.teacher_agent import TeacherAgent
from app.agents.debugger_agent import DebuggerAgent
from app.agents.content_agent import ContentAgent
from app.agents.motivator_agent import MotivatorAgent
from app.schema import DoubtRequest, DoubtResponse

class Orchestrator:
    def __init__(self):
        self.teacher = TeacherAgent()
        self.debugger = DebuggerAgent()
        self.content = ContentAgent()
        self.motivator = MotivatorAgent()

    def handle(self, request: DoubtRequest) -> DoubtResponse:
        explanation = self.teacher.run(request.doubt)
        debug = self.debugger.run(request.code or "")
        quiz = self.content.run(request.doubt)
        motivation = self.motivator.run()
        
        return DoubtResponse(
            explanation=explanation,
            debug=debug,
            quiz=quiz,
            motivation=motivation
        )
