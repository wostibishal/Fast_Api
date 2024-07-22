from fastapi import Depends, FastAPI
from .schemas import Blog
from . import  models
from .database import engine, SessionLocal
from sqlalchemy import Session

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/blog')
def create(request:Blog, db:Session = Depends(get_db)):
    new_blog = models.Blog(title= request.title, body= request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog