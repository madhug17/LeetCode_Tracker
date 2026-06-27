from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from services.leetcode_service import (
    sync_leetcode_data,
    get_leetcode_profile,
    get_cache_profile
)
from services.notification_service import (
    create_notification
)
from core.dependencies import (
    get_current_user
)
router = APIRouter(
    prefix="/leetcode",
    tags=["Leetcode"]
)
@router.get("/profile")
def leetcode_profile(
    current_user=Depends(get_current_user)
):
    return get_leetcode_profile(
        current_user.leetcode_username
    )
@router.post("/sync")
def sync_profile(
    db: Session = Depends(get_db),
    current_user = Depends(
        get_current_user
    )
):
    result = sync_leetcode_data(
        db,
        current_user
    )
    create_notification(

        db=db,
        user_id=current_user.id,
        title="LeetCode Sync",
        message="Your LeetCode profile synced successfully 🚀"
    )
    return result
@router.get("/cached-profile")
def get_profile(
    current_user = Depends(
        get_current_user
    )
):
    return get_cache_profile(
        current_user
    )