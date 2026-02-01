from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class SolutionItem(BaseModel):
    problem_index: int
    content_snippet: str
    correct_answer: str
    points: int = 1

class TestInstance(BaseModel):
    id: str = Field(..., alias="_id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    teacher_id: Optional[str] = None
    grade: str
    topic: str
    solutions: List[SolutionItem]

    class Config:
        populate_by_name = True
