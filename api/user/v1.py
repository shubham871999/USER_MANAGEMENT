from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.users import service, schemas
from core.database.session import get_db

router = APIRouter()

@router.post("/", response_model=schemas.UserResponse)
def create_user(user_in: schemas.UserCreate, db: Session = Depends(get_db)):
    return service.create_user(db, user_in)

@router.get("/{user_id}", response_model=schemas.UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return service.get_user_by_id(db, user_id)

@router.get("/", response_model=list[schemas.UserResponse])
def list_all_users(db: Session = Depends(get_db)):
    return service.list_users(db)