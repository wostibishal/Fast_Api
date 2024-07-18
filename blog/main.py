from fastapi import Depends, FastAPI
from .schemas import Blog
from .models import  Base
from .database import engine
from sqlalchemy import Session

app = FastAPI()

Base.metadata.create_all(engine)

@app.post('/blog')
def create(blog: Blog, db:Session = Depends(get_db)):
    return db