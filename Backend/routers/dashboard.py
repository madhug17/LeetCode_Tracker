from fastapi import APIRouter , Depends 
from sqlalchemy.orm import Session
from database.db import get_db
from core.dependencies import get_current_user
from services.dashboard_service import get_dashboard_stats,get_user_progress
from services.ai_service import generate_ai_recommendantion
router = APIRouter()
@router.get('/stats')
def dashboard_stats(
    db:Session = Depends(get_db), # connection with the database 
    current_user = Depends(get_current_user) # only logged in people will access this man 
):
    return get_dashboard_stats(
        db,
        current_user
    )#Router → Service → Database
@router.get('/progress')
def user_progress(
    db:Session=Depends(get_db),
    current_user = Depends(get_current_user)
):
    return get_user_progress(
        db,
        current_user
    )
@router.get('/ai-recommendation')
def ai_recommendation(
    currrent_user=Depends(get_current_user)
):
    return generate_ai_recommendantion(
        currrent_user.problems 
    )