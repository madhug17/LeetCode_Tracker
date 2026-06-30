
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends 
from core.dependencies import get_current_user,get_db
from services.streak_service import get_consistency_tracking, get_current_streak,get_heatmap_data, get_longest_streak
router = APIRouter(
    prefix="/streak",
    tags=["Streak"]
)
@router.get("/all")
def get_all_streaks(
    db:Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    current_data = get_current_streak(
        db,current_user
    )
    longest_data = get_longest_streak(
        db,current_user
    )
    consistency_data = get_consistency_tracking(
        db,
        current_user
    )
    return {

        "current_streak":
        current_data["current_streak"],

        "longest_streak":
        longest_data["longest_streak"],

        "active_days":
        consistency_data["active_days"],

        "consistency_percentage":
        consistency_data["consistency_percentage"]

    }
@router.get('/heatmap')
def heatmap(
    db:Session=Depends(get_db),
    current_user = Depends(get_current_user)
):
    return get_heatmap_data(
        db,current_user
    )