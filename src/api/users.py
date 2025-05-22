from typing import Annotated

from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post("")
async def add_user():
    return {"user_id": 1}