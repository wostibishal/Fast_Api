from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from blog import models, schemas

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def blog_by_id(id:int, db: Session ):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not found")
    return blog

def create(request:schemas.Blog, db:Session):
    new_blog = models.Blog(title= request.title, body= request.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def update(id:int, request:schemas.Blog, db:Session):
    blog_query = db.query(models.Blog).filter(models.Blog.id == id)
    blog_query = db.query(models.Blog).filter(models.Blog.id == id)
    blog = blog_query.first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    try:
        blog_query.update(request.dict())
        db.commit()
        db.refresh(blog)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    return blog

def destroy(id:int, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return blog