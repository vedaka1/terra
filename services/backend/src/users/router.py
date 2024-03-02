import uuid
from typing import Dict, List, Optional

from fastapi import APIRouter, Depends, Request, Response, status
from fastapi.security import OAuth2PasswordRequestForm

from src.config import settings
from src.exceptions import (
    InvalidCredentialsException,
    InvalidTokenException,
    TokenExpiredException,
)

from .dependencies import get_current_active_user
from .models import UserModel
from .schemas import Friend, FriendCreateDB, Token, User, UserCreate, UserToUser
from .service import AuthService, UserService

auth_router = APIRouter(prefix="/auth", tags=["Auth"])
user_router = APIRouter(prefix="/users", tags=["Users"])


@auth_router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user: UserCreate) -> User:
    return await UserService.register_new_user(user)  # type: ignore


@auth_router.post("/login")
async def login(
    response: Response, credentials: OAuth2PasswordRequestForm = Depends()
) -> Token:
    user = await AuthService.authenticate_user(
        credentials.username, credentials.password
    )
    if not user:
        raise InvalidCredentialsException
    token = await AuthService.create_token(user.id)
    response.set_cookie(
        "access_token",
        token.access_token,
        max_age=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
        httponly=True,
    )
    response.set_cookie(
        "refresh_token",
        token.refresh_token,
        max_age=settings.REFRESH_TOKEN_EXPIRE_DAYS * 30 * 24 * 60,
        httponly=True,
    )
    return token


@auth_router.post("/logout")
async def logout(
    request: Request,
    response: Response,
    user: UserModel = Depends(get_current_active_user),
):
    response.delete_cookie("access_token")
    response.delete_cookie("refresh_token")
    await AuthService.logout(request.cookies.get("refresh_token"))
    return {"message": "Logged out successfully"}


@auth_router.post("/refresh")
async def refresh_token(request: Request, response: Response) -> Token:
    new_token = await AuthService.refresh_token(
        uuid.UUID(request.cookies.get("refresh_token"))
    )

    response.set_cookie(
        "access_token",
        new_token.access_token,
        max_age=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
        httponly=True,
    )
    response.set_cookie(
        "refresh_token",
        new_token.refresh_token,
        max_age=settings.REFRESH_TOKEN_EXPIRE_DAYS * 30 * 24 * 60,
        httponly=True,
    )
    return new_token


@user_router.get("/me")
async def get_current_user(
    current_user: UserModel = Depends(get_current_active_user),
) -> User:
    return await UserService.get_user(current_user.id)


@user_router.get("")
async def get_all_users(
    offset: Optional[int] = 0,
    limit: Optional[int] = 100,
) -> List[User]:
    return await UserService.get_users_list(offset=offset, limit=limit)


@user_router.get("/{user_id}")
async def get_user(user_id: str) -> User:
    return await UserService.get_user(user_id)


@user_router.post("/me/friends")
async def add_friend(
    friend_id: str, current_user: UserModel = Depends(get_current_active_user)
) -> uuid.UUID:
    return await UserService.add_friend(user_id=current_user.id, friend_id=friend_id)


@user_router.delete("/me/friends/{friend_id}")
async def delete_friend(
    friend_id: str, current_user: UserModel = Depends(get_current_active_user)
) -> None:
    return await UserService.delete_friend(user_id=current_user.id, friend_id=friend_id)


@user_router.get("/me/friends")
async def get_all_user_friends(
    offset: Optional[int] = 0,
    limit: Optional[int] = 100,
    current_user: UserModel = Depends(get_current_active_user),
) -> List[Friend]:
    return await UserService.get_user_friends_list(
        current_user.id, offset=offset, limit=limit
    )
