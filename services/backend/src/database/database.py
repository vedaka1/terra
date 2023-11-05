import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import URL, text, insert, select
from .models import UserTable
from .config import *

engine = create_async_engine(
    url=f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
    echo=True
)

session_fabric = async_sessionmaker(engine, expire_on_commit=False)

async def test():
    # async with engine.connect() as conn:
        # await conn.execute(insert(user_table).values(
        #     {"user_id": 12345, "echo_mode": False, "username": "test"}
        # ))
        # res = await conn.execute(text("SELECT * FROM tg_bot.users"))
        # print(res.fetchall())
        # await conn.commit()
    async with session_fabric() as session:
        res = await session.execute(select(UserTable))
        users = res.all()
        print(users)
        

# asyncio.run(test())