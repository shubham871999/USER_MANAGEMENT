from sqlalchemy.orm import Session
from services.users import models, schemas
from core.common.utils import hash_password
from core.common.exceptions import UserNotFound

def create_user(db: Session, user_in: schemas.UserCreate):
    user = models.User(
        username=user_in.username,
        email=user_in.email,
        hashed_password=hash_password(user_in.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_id(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise UserNotFound
    return user

def list_users(db: Session):
    return db.query(models.User).all()
