# src/app/api/api_v1.py
from fastapi import APIRouter
from app.api.routes import user

api_router = APIRouter()
api_router.include_router(user.router, prefix="", tags=["users"])