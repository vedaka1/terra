from fastapi import APIRouter
from src.schemas.users import UserIn, UserOut
import src.crud.user as crud

router = APIRouter()

@router.post("/register", response_model=UserIn)
async def register(user: UserIn):
    return await crud.create_user(user)

@router.get("/users/{username}", response_model=UserOut)
async def get_user(username: str):
    return await crud.get_user(username)

@router.post("/user/{username}")
async def delete_user(username: str):
    return await crud.delete_user(username)