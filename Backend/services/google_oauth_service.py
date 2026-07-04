from google.oauth2 import id_token
from google.auth.transport import requests
from sqlalchemy.orm import Session
from models.user import User
from utils.security import hash_password
from utils.jwt_handling import create_access_token
from dotenv import load_dotenv
import os
load_dotenv()
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
def google_login(
        db:Session,
        token:str
):
    idinfo = id_token.verify_oauth2_token(
        token,requests.Request(),
        GOOGLE_CLIENT_ID
    )
    email = idinfo['email']
    username= idinfo.get(
        "name",
        email.split("@")[0]
    )
    user = db.query(User).filter(
        User.email == email
    ).first()
    if not user:
        user = User(
            username = username,
            email = email,
            password=hash_password(
                "google_oauth_user"
            )

        )
        db.add(user)
        db.commit()
        db.refresh(user)
    access_token = create_access_token(
        data = {
            "sub":user.email
        }
    )
    return{
        "access_token":access_token,
        "token_type":"bearer",
        "user":{
            "id":user.id,
            "username":user.username,
            "email":user.email
        }
    }

