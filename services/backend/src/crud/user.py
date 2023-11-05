from src.database.database import session_fabric
from src.database.models import UserTable
from src.schemas.users import UserIn, UserOut

from sqlalchemy.exc import IntegrityError
from sqlalchemy import insert,delete
from passlib.context import CryptContext
from fastapi import HTTPException

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def create_user(user: UserIn):
    async with session_fabric() as session:
        user.user_password = pwd_context.encrypt(user.user_password)
        try:
            stmt = insert(UserTable).values(user.model_dump())
            result = await session.execute(stmt)
            print(result)
            await session.commit()
            return 200
        except IntegrityError:
            raise HTTPException(status_code=401,
                                detail=f"Sorry, that username already exists.")

async def get_user(username: int) -> UserOut:
    async with session_fabric() as session:
        user = await session.get(UserTable, username)
        return UserOut.model_validate({
            "user_email": user.user_email,
            "username": user.username
        })

async def delete_user(user_id: int):
    async with session_fabric() as session:
        stmt = delete(UserTable).where(UserTable.user_id == user_id)
        await session.execute(stmt)
        await session.commit()
        return 200
