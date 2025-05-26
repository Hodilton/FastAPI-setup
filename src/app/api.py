# src/app/api.py
from fastapi import APIRouter
from app.auth import router as auth_router
from app.users import router as users_router
from app.items import router as items_router

api_router = APIRouter()
api_router.include_router(auth_router, prefix="/auth", tags=["auth"])
api_router.include_router(users_router, prefix="/users", tags=["users"])
api_router.include_router(items_router, prefix="/items", tags=["items"])
