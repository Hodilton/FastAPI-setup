# src/app/auth.py
from fastapi import APIRouter, Depends, HTTPException, status, Form
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session, select
from jose import jwt
from app.models import Token, TokenPayload, User
from app.security import verify_password, create_access_token
from app.db import get_db
from app.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")
router = APIRouter()

@router.post("/token", response_model=Token)
def login_for_access_token(
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
):
    user = authenticate(db, email=username, password=password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token = create_access_token(user.id)
    return {"access_token": access_token, "token_type": "bearer"}

def authenticate(db: Session, email: str, password: str) -> User | None:
    user = db.exec(select(User).where(User.email == email)).first()
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user

def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)) -> User:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        token_data = TokenPayload(**payload)
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    user = db.get(User, token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def get_current_active_superuser(current_user: User = Depends(get_current_user)) -> User:
    if not current_user.is_superuser:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return current_user
