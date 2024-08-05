from sqlalchemy.orm import Session

from blog import models


def auth(id: int, db: Session , username: str, password: str):
    user = user = db.query(models.User).filter(models.User.id == id).first()