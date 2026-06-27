from fastapi import APIRouter , Depends
from core.premium_dependencies import get_premium_user
router = APIRouter(
    prefix="/premium",
    tags = ['only-Premium']
)
@router.get("/premium-stats")
def premium_stats(
    premium_user= Depends(get_premium_user)
):
    return{
        "Message":"Premium analytics"
    }