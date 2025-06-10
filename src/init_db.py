# src/init_db.py
from app.database.session import init_db
from app.models import user

if __name__ == "__main__":
    import asyncio
    asyncio.run(init_db())