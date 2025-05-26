# src/app/items.py
from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from app.models import Item, ItemCreate, ItemPublic, User
from app.auth import get_current_user
from app.db import get_db

router = APIRouter()

@router.post("/", response_model=ItemPublic)
def create_item(item: ItemCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_item = Item(**item.dict(), owner_id=current_user.id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/", response_model=list[ItemPublic])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.exec(select(Item).where(Item.owner_id == current_user.id).offset(skip).limit(limit)).all()
