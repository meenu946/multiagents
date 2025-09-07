from fastapi import FastAPI
from app.orchestrator import Orchestrator
from app.schema import DoubtRequest, DoubtResponse

app = FastAPI(title="EduNinja Agents")

orchestrator = Orchestrator()

@app.post("/solve-doubt", response_model=DoubtResponse)
def solve_doubt(request: DoubtRequest):
    return orchestrator.handle(request)
