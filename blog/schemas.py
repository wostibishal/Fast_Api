from typing import List, Optional
from pydantic import BaseModel



class Blog(BaseModel):
    title: str
    body: str

    class config:
        orm_mode = True

class User(BaseModel):
    name:str
    email: str
    password: str

class UserView(BaseModel):
    name:str
    email: str
    blogs : List[Blog]=[]
    class config():
        orm_mord = True

class ShowBlog(BaseModel):
    title: str
    body: str
    creator : UserView

    class config():
        orm_mord = True

class Login(BaseModel):
    username: str
    password: str

    class config():
        orm_mord = True

class TokenResponse(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None