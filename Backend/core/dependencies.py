from typing import final
from database.db import SessionLocal
from sqlalchemy.orm import Session # ORM Object Relational Mapping 
from models.user import User
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,HTTPException 
from utils.jwt_handling import verify_token
oauth2_schema = OAuth2PasswordBearer(
    tokenUrl='/auth/login'
)
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
oauth2_schema = OAuth2PasswordBearer(
    tokenUrl='/auth/login'
)
def get_current_user(
token: str = Depends(oauth2_schema),
db: Session = Depends(get_db)
):
    payload= verify_token(token)
    if not payload:
        raise HTTPException(
            status_code = 401,
            detail ="Invalid token"
        )
    email = payload.get("sub")
    db_user=db.query(User).filter(User.email==email).first()
    if not db_user:
        raise HTTPException(
            status_code = 404,
            detail="User not found"
        )
    return db_user
