from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str

    class config:
        orm_mode = True

class ShowBlog(BaseModel):
    title: str
    body: str
    class config():
        orm_mord = True

class User(BaseModel):
    name:str
    email: str
    password: str