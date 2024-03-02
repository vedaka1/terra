import uuid
from typing import Optional

from pydantic import BaseModel, Field


class UserBase(BaseModel):
    email: Optional[str] = Field(None)
    username: Optional[str] = Field(None)
    is_active: bool = Field(True)
    is_verified: bool = Field(False)
    is_superuser: bool = Field(False)


class UserCreate(UserBase):
    email: str
    username: str
    password: str


class UserUpdate(UserBase):
    password: Optional[str] = None


class User(UserBase):
    id: uuid.UUID
    email: str
    username: str
    is_active: bool
    is_verified: bool
    is_superuser: bool

    class Config:
        from_attributes = True


class UserCreateDB(UserBase):
    hashed_password: Optional[str] = None


class UserUpdateDB(UserBase):
    hashed_password: str


class UserToUser(BaseModel):
    user_id: uuid.UUID
    friend_id: uuid.UUID


class Friend(User):
    pass


class FriendCreateDB(BaseModel):
    user_id: uuid.UUID


class FriendUpdateDB(FriendCreateDB):
    user_id: Optional[uuid.UUID] = Field(None)


class RefreshSessionCreate(BaseModel):
    refresh_token: uuid.UUID
    expires_in: int
    user_id: uuid.UUID


class RefreshSessionUpdate(RefreshSessionCreate):
    user_id: Optional[uuid.UUID] = Field(None)


class Token(BaseModel):
    access_token: str
    refresh_token: uuid.UUID
    token_type: str
