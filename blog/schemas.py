from typing import List
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
    blogs : List
    class config():
        orm_mord = True

class ShowBlog(BaseModel):
    title: str
    body: str
    creator : UserView

    class config():
        orm_mord = True
