# This services is mainly used for connecting with user to databse 
#from routers import leetcode
from sqlalchemy.orm import Session  
from utils.jwt_handling import create_access_token,create_refesh_token
from models.user import User
from fastapi import HTTPException
from utils.security import hash_password, verify_password
def create_user(db, user_data):
    hashed_password = hash_password(user_data.password)
    new_user = User(
        username=user_data.username,
        email=user_data.email,
        password=hashed_password,
        is_premium=user_data.is_premium,
        leetcode_username= user_data.leetcode_username,
        bio = user_data.bio
        #Forget_password  =user_data.Forget_password,
        #is_verified=False
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
def login_user(db: Session, username: str, password:str):
    db_user = db.query(User).filter(User.username == username).first()
    if not db_user:
        raise HTTPException(
            status_code = 404,
            detail= "User not found"
        )
        #return {"message": "User not found"}
    if not verify_password(password, db_user.password):
        raise HTTPException(
            status_code = 401,
            detail = "Invalid password"
        )
        #return {"message": "Invalid password"}
    #if not db_user.username != user.username:
    #    return{"Message":"Invaild username"}
    #if not db_user.is_premium:
    #    return{"Message":"Please take premium account "}
    access_token = create_access_token(
        data={
            "sub": db_user.email
        }
    )
    refresh_token= create_refesh_token(
        data={
            "sub":db_user.email
        }
    )
    return{
        "access_token":access_token,
        "refresh_token":refresh_token,
        "token_type":"bearer"
    }

