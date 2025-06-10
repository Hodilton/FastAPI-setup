# src/app/api/routes/user.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_async_session
from app.repositories.user import UserRepository
from app.services.user import UserService
from app.schemas.user import UserCreate, UserRead

router = APIRouter()

@router.post("/users/", response_model=UserRead)
async def create_user(user_in: UserCreate, db: AsyncSession = Depends(get_async_session)):
    repository = UserRepository(db)
    service = UserService(repository)

    existing_user = await service.get_user_by_email(user_in.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = await service.create_user(user_in)
    return user