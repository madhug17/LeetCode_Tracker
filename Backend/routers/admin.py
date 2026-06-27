from fastapi import APIRouter , Depends
from core.admin_dependencies import get_admin_user
router = APIRouter(
    prefix='/admin',
    tags = ['Admin']
)
@router.get('/admin-only')
def admin_router(
    admin = Depends(get_admin_user)
):
    return{
        "message": "Welcome admin mawa"
    }