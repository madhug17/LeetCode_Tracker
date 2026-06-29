

from models.user import User
from core.dependencies import get_current_user
from utils.jwt_handling import create_access_token,verify_token
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from core.dependencies import get_current_user
from schemas.password_reset import ForgetPassRequest,ResetPasswordRequest
from pydantic import BaseModel

from schemas.user_schema import UserCreate, UserLogin
from services.auth_service import create_user, login_user
from core.dependencies import get_current_user, get_db
from fastapi.security import OAuth2PasswordRequestForm
from services.email_service import sent_email

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)
@router.post("/register")
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return create_user(db, user)
@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    #user: UserLogin,
    db: Session = Depends(get_db)
):
    return login_user(db, form_data.username,form_data.password)
@router.post("/refresh")
def refresh_token(refresh_token:str):
    payload = verify_token(refresh_token)
    email= payload.get("sub")
    new_access_token = create_access_token(
        data={
            "sub":email
        }
    )
    return {
        "access_token":new_access_token
    }
@router.get("/me")
def get_me(curr_user=Depends(get_current_user)):
    return{
        "message": "Proteected route Success",
        "User": curr_user
    }
@router.get("/verify-email")
def verify_email(token:str,db:Session=Depends(get_db)):
    payload = verify_token(token)
    email = payload.get("sub")
    db_user= db.query(User).filter(User.email==email).first()
    db_user.is_verified = True
    db.commit()
    return{
        "Message":"Email Verified Successfully"
    }
@router.post('/forget-password')
def forget_password(
    request:ForgetPassRequest,
    db: Session = Depends(get_db)
):
    return {
        "message":"Forget password endpoint working"
    }
@router.post('/reset-password')
def reset_password(
    request:ResetPasswordRequest,
    db: Session=Depends(get_db)
):
    return{
        "message":"Reset Password endpoint working"
    }
@router.get("/test-email")
async def test_email(
    current_user=Depends(
        get_current_user
    )
):
    await sent_email(
        email="YOUR_EMAIL@gmail.com",
        subject="LeetCode Tracker Test",
        body=f"""
        <h1>Email Working </h1>
        <p> Hello {current_user.username}</p>
        <p>Backend email system working successfully </p>
        <p> You have sync with Leetcode id {current_user.leetcode_username}</p>
        <p>Keep grinding DSA 😎🔥</p>
        <hr>
        <p>LeetCode Tracker Team</p>
        
           """
    )
    return{
        "message":"Email sent successfully "
    }
class GoogleToken(BaseModel):
    token:str
@router.post('/google-login')
def google_login():
    pass