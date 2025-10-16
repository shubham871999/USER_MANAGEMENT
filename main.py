from fastapi import FastAPI
from api.user.v1 import router as user_router
from api.auth.v1 import router as auth_router

app = FastAPI(title="User Management API", version="1.0")

# Routers
app.include_router(user_router, prefix="/api/v1/users", tags=["Users"])
app.include_router(auth_router, prefix="/api/v1/auth", tags=["Auth"])

@app.get("/", tags=["Health"])
def health_check():
    return {"status": "ok", "message": "User Management API running"}
