from fastapi import FastAPI
from database.db import engine
from database.db import Base
from models.user import User
from models.problem import Problem
from models.notification import Notification
from routers.auth import router as auth_router
from routers.problem import router as problem_router
from routers.leetcode import router as leetcode_router
from routers.notification import router as notification_router
#from routers.payment import router as payment_router
from routers.dashboard import router as dashboard_router
from services.background_jobs import scheduler
from fastapi.middleware.cors import CORSMiddleware
from routers import streak

app = FastAPI()
Base.metadata.create_all(bind=engine)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)



@app.get("/")
def home():
    return {
        "message": "LeetCode Tracker API Running 🚀"
    }


app.include_router(auth_router)
app.include_router(problem_router)
app.include_router(leetcode_router)
app.include_router(notification_router)
app.include_router(streak.router)

#app.include_router(payment_router)

app.include_router(
    dashboard_router,
    prefix="/dashboard",
    tags=["Dashboard"]
)

# Start Scheduler

@app.on_event("startup")
def start_scheduler():
    scheduler.start()
    print("Background scheduler started 🚀")
