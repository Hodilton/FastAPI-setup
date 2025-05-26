# src/app/users.py
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.models import User, UserCreate, UserPublic
from app.auth import get_current_user, get_current_active_superuser
from app.db import get_db
from app.security import get_password_hash

router = APIRouter()

@router.post("/", response_model=UserPublic)
def create_user(user: UserCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_superuser)):
    db_user = db.exec(select(User).where(User.email == user.email)).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user.password)
    new_user = User(email=user.email, hashed_password=hashed_password, full_name=user.full_name, is_superuser=user.is_superuser)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/me", response_model=UserPublic)
def read_user_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.get("/", response_model=list[UserPublic])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_superuser)):
    return db.exec(select(User).offset(skip).limit(limit)).all()
