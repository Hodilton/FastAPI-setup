# src/app/db.py
from sqlmodel import Session, SQLModel, create_engine, select
from app.config import settings

engine = create_engine(settings.DATABASE_URL)

def get_db():
    with Session(engine) as session:
        yield session

def init_db():
    from app.models import User
    from app.security import get_password_hash

    SQLModel.metadata.create_all(engine)
    with Session(engine) as db:
        user = db.exec(select(User).where(User.email == settings.FIRST_SUPERUSER)).first()
        if not user:
            user = User(
                email=settings.FIRST_SUPERUSER,
                hashed_password=get_password_hash(settings.FIRST_SUPERUSER_PASSWORD),
                is_superuser=True,
            )
            db.add(user)
            db.commit()
