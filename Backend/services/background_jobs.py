from apscheduler.schedulers.background import BackgroundScheduler
from database.db import SessionLocal
from models.user import User
from services.leetcode_service import sync_leetcode_data
scheduler = BackgroundScheduler()
def sync_all_users():
    db = SessionLocal()
    try:
        users = db.query(User).all()
        for user in users:
            if user.leetcode_username:
                print(
                    f"Syncing {user.username}"
                )
                sync_leetcode_data(
                    db,
                    user
                )
        print("Background sync complete")
    finally:
        db.close()
scheduler.add_job(
    sync_all_users,
    "interval",
    minutes = 10
)