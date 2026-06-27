from fastapi import APIRouter , Depends
from sqlalchemy.orm import Session
from database.db import get_db
from core.dependencies import get_current_user
from models.notification import Notification
router = APIRouter(
    prefix ='/notification',
    tags=["Notification"]
)
@router.get('/')
def get_notification(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    notification = db.query(Notification).filter(
        Notification.user_id == current_user.id
    ).all()
    return notification