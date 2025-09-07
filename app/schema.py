from pydantic import BaseModel

class DoubtRequest(BaseModel):
    doubt: str
    code: str | None = None

class DoubtResponse(BaseModel):
    explanation: str
    debug: str
    quiz: str
    motivation: str
