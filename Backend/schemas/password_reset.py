from pydantic import BaseModel
from pydantic import EmailStr
class ForgetPassRequest(
    BaseModel
):
    email:EmailStr
class ResetPasswordRequest(
    BaseModel
):
    token : str
    new_password : str 