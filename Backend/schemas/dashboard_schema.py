from pydantic import BaseModel
class DailyProgress(BaseModel):
    date: str
    count: int 
class ProgressResponse(BaseModel):
    total_solved : int
    week: int 
    daily_progress: list[DailyProgress] #Samelist Comes for the class Dailyprocess
