# --- Add these lines at the top of service.py ---

import os
import sys

# Get the absolute path to the project root (USER_MANAGEMENT)
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(CURRENT_DIR)))

# Add the project root to sys.path if it's not already there
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# --- Now normal imports will work ---
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.users.schemas import UserResponse, UserBase, UserCreate
from core.database.session import get_db
from services.users import service  # ✅ only import AFTER sys.path fix

router = APIRouter(prefix="/users", tags=["Users"])

# ✅ Class-based route handler
class UserRouter:

    @staticmethod
    @router.post("/", response_model=UserResponse)
    def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
        """Create a new user"""
        return service.create_user(db, user_in)

    @staticmethod
    @router.get("/{user_id}", response_model=UserResponse)
    def get_user(user_id: int, db: Session = Depends(get_db)):
        """Get a user by ID"""
        return service.get_user_by_id(db, user_id)

    @staticmethod
    @router.get("/", response_model=list[UserResponse])
    def list_all_users(db: Session = Depends(get_db)):
        """List all users"""
        return service.list_users(db)
