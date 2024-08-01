from typing import List
from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from blog import  schemas, database
from blog.repository import blog


router = APIRouter(
    prefix="/bog",
    tags=['blogs'],
)

@router.get('/', status_code=200, response_model= List[schemas.ShowBlog])
def all(db:Session = Depends(database.get_db)):
    return blog.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog, db:Session = Depends(database.get_db)):
    return blog.create(request, db)

@router.get('/{id}/', status_code=200)
def blog_by_id(id, response:Response, db:Session = Depends(database.get_db)):
    return blog.blog_by_id(id,db)

@router.put('/{id}/', response_model=schemas.ShowBlog, status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.update(id, request, db)

@router.delete('/{id}/', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db:Session = Depends(database.get_db)):
    return blog.destroy(id, db)