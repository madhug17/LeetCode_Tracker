from pydantic import BaseModel
from typing import Optional


class ProblemCreate(BaseModel):

    title: str
    difficulty: str
    topic: Optional[str] = None
    time_spend: Optional[int] = None
    notes: Optional[str] = None


class ProblemUpdate(BaseModel):

    title: Optional[str] = None
    difficulty: Optional[str] = None
    topic: Optional[str] = None
    time_spend: Optional[int] = None
    notes: Optional[str] = None