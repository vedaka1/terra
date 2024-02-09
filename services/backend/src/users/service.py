import uuid
from datetime import datetime, timedelta, timezone
from typing import Optional

from fastapi import HTTPException, status
from passlib.context import CryptContext
from jose import jwt

from src.database import async_session_factory
from src.config import settings
from .dao import UserDAO, RefreshSessionDAO
from .models import UserModel, RefreshSessionModel
from .schemas import User, UserCreate, UserCreateDB, Token, RefreshSessionCreate, RefreshSessionUpdate
from .utils import get_password_hash, is_valid_password


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthService:
    @classmethod
    async def create_token(cls, user_id: uuid.UUID) -> Token:
        access_token = cls._create_access_token(user_id)
        refresh_token_expires = timedelta(
            days=settings.REFRESH_TOKEN_EXPIRE_DAYS
        )
        refresh_token = cls._create_refresh_token()
        async with async_session_factory() as session:
            await RefreshSessionDAO.add(
                session,
                RefreshSessionCreate(
                    user_id=user_id,
                    refresh_token=refresh_token,
                    expires_in=refresh_token_expires.total_seconds()
                )
            )
            await session.commit()
        return Token(
            access_token=access_token,
            refresh_token=refresh_token,
            token_type='bearer'
        )
    
    @classmethod
    async def authenticate_user(cls, username: str, password: str) -> Optional[UserModel]:
        async with async_session_factory() as session:
            db_user = await UserDAO.find_one_or_none(session, username=username)
        if db_user and is_valid_password(password, db_user.hashed_password):
            return db_user
        return None

    @classmethod
    async def logout(cls, token: uuid.UUID) -> None:
        async with async_session_factory() as session:
            refresh_session = await RefreshSessionDAO.find_one_or_none(session, RefreshSessionModel.refresh_token == token)
            print(refresh_session.id)
            if refresh_session:
                await RefreshSessionDAO.delete(session, id=refresh_session.id)
            await session.commit()

    @classmethod
    def _create_access_token(cls, user_id: uuid.UUID) -> str:
        to_encode = {
            'sub': str(user_id),
            'exp': datetime.utcnow() + timedelta(
                minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
            )
        }
        encoded_jwt = jwt.encode(
            to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
        )
        return f'Bearer {encoded_jwt}'
    
    @classmethod
    def _create_refresh_token(cls) -> str:
        return uuid.uuid4()


class UserService:
    @classmethod
    async def register_new_user(cls, user: UserCreate) -> UserModel:
        async with async_session_factory() as session:
            user_exist = await UserDAO.find_one_or_none(session, email=user.email)
            if user_exist:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT, detail="User already exists")

            user.is_superuser = False
            user.is_verified = False
            db_user = await UserDAO.add(
                session,
                UserCreateDB(
                    **user.model_dump(),
                    hashed_password=get_password_hash(user.password))
            )
            await session.commit()
        return db_user
    
    @classmethod
    async def get_user(cls, user_id: uuid.UUID) -> UserModel:
        async with async_session_factory() as session:
            db_user = await UserDAO.find_one_or_none(session, id=user_id)
        if db_user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return db_user

    @classmethod
    async def get_users_list(cls, *filter, offset: int = 0, limit: int = 100, **filter_by) -> list[UserModel]:
        async with async_session_factory() as session:
            users = await UserDAO.find_all(session, *filter, offset=offset, limit=limit, **filter_by)
        if users is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Users not found")
        return users
