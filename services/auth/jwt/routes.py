from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database.session import get_db
from core.common.utils import verify_password
from core.common.exceptions import InvalidCredentials
from services.users.models import User
from services.auth.jwt import service, schemas

router = APIRouter()

@router.post("/login", response_model=schemas.TokenResponse)
def login(token_req: schemas.TokenRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == token_req.username).first()
    if not user or not verify_password(token_req.password, user.hashed_password):
        raise InvalidCredentials

    token = service.create_access_token({"sub": user.username})
    return {"access_token": token}
