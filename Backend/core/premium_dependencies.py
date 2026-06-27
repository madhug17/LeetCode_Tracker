from fastapi import HTTPException ,Depends
from core.dependencies import get_current_user
def get_premium_user(
        current_user=Depends(get_current_user)
):
    if not get_premium_user:
        raise HTTPException(
            status_code=403,
            detail="Premium membership required"
        )
    return current_user
