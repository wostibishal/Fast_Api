from typing import List
from fastapi import APIRouter, Depends
from requests import Session
from blog import schemas, database
from blog.repository import user


router = APIRouter(
    prefix="/users",
    tags=['users'],
)

@router.post('/', response_model=schemas.UserView, tags=['User'])
def creare_user(request: schemas.User, db:Session = Depends(database.get_db)):
    return user.create(request, db)

@router.get('/{id}', response_model=schemas.UserView, tags=['User'] )
def view_user(id:int, db:Session = Depends(database.get_db)):
    return user.view(id,db)