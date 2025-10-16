from fastapi import APIRouter
from services.auth.jwt.routes import router as jwt_routes

router = APIRouter()
router.include_router(jwt_routes)
