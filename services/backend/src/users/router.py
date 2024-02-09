from typing import Optional, List

from fastapi import APIRouter, status, Response, Depends, Request
from fastapi.security import OAuth2PasswordRequestForm

from src.exceptions import InvalidCredentialsException, InvalidTokenException, TokenExpiredException
from src.config import settings
from .schemas import User, UserCreate, Token
from .service import UserService, AuthService
from .dependencies import get_current_user, get_current_superuser, get_current_active_user
from .models import UserModel


auth_router = APIRouter(prefix='/auth', tags=['Auth'])
user_router = APIRouter(prefix='/user', tags=['User'])


@auth_router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(
    user: UserCreate
) -> User:
    return await UserService.register_new_user(user)


@auth_router.post("/login")
async def login(
    response: Response,
    credentials: OAuth2PasswordRequestForm = Depends()
) -> Token:
    user = await AuthService.authenticate_user(credentials.username, credentials.password)
    if not user:
        raise InvalidCredentialsException
    token = await AuthService.create_token(user.id)
    response.set_cookie(
        'access_token',
        token.access_token,
        max_age=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
        httponly=True
    )
    response.set_cookie(
        'refresh_token',
        token.refresh_token,
        max_age=settings.REFRESH_TOKEN_EXPIRE_DAYS * 30 * 24 * 60,
        httponly=True
    )
    return token


@auth_router.post("/logout")
async def logout(
    request: Request,
    response: Response,
    user: UserModel = Depends(get_current_active_user),
):
    await AuthService.logout(request.cookies.get('refresh_token'))
    response.delete_cookie('access_token')
    response.delete_cookie('refresh_token')
    return {"message": "Logged out successfully"}


@user_router.get("/me")
async def get_current_user(
    current_user: UserModel = Depends(get_current_active_user)
) -> User:
    return await UserService.get_user(current_user.id)


@user_router.get("/all")
async def get_all_users(
    offset: Optional[int] = 0,
    limit: Optional[int] = 100,
) -> List[User]:
    return await UserService.get_users_list(offset=offset, limit=limit)