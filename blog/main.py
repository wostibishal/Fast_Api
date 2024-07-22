from fastapi import Depends, FastAPI, HTTPException, Response, status
from .schemas import Blog
from . import  models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return{"message": "hello world"}

@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create(request:Blog, db:Session = Depends(get_db)):
    new_blog = models.Blog(title= request.title, body= request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get('/blog', status_code=200)
def all(db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get('/blog/{id}', status_code=200)
def show(id, response:Response, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail':f"Blog with the id {id} is not found"}
    return blog

@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id,request: Blog, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).update(request)
    return blog

@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db:Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return 'done'
