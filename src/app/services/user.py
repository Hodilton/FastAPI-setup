# src/app/services/user.py
from app.repositories.user import UserRepository
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import get_password_hash

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def create_user(self, user_in: UserCreate) -> User:
        hashed_password = get_password_hash(user_in.password)
        user = User(
            email=user_in.email,
            hashed_password=hashed_password,
            is_active=True,
            is_superuser=False
        )
        return await self.repository.create(user)

    async def get_user_by_email(self, email: str) -> User | None:
        return await self.repository.get_by_email(email)