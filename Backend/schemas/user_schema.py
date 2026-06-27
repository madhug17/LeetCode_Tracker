from pydantic import BaseModel # basemodel is like how your data should looks like number of entities
class UserCreate(BaseModel):
    username: str
    email : str
    password : str
    is_premium : bool = False
    leetcode_username: str
    bio:str
    #Forget_password : bool=False
class UserLogin(BaseModel):
    email: str
    password: str
