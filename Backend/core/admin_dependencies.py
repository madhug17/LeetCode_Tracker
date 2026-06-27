from fastapi import HTTPException, Depends
from core.dependencies import get_current_user
def get_admin_user(
        current_user = Depends(get_current_user)
):
    if not current_user.is_admin:
        raise HTTPException(
            detail="Admin access required",
            status_code=403
        )
    return current_user