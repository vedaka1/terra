import datetime
import uuid
from typing import Optional

from pydantic import BaseModel, Field


class MessageBase(BaseModel):
    chat_id: int
    user_id: uuid.UUID
    content: str


class MessageCreate(MessageBase):
    pass


class MessageUpdate(MessageBase):
    id: int
    user_id: uuid.UUID
    content: str


class Message(MessageBase):
    id: int
    chat_id: int
    user_id: uuid.UUID
    created_at: datetime.datetime
    content: str

    class Config:
        from_attributes = True


class ChatBase(BaseModel):
    name: Optional[str] = Field(None)
    owner_id: uuid.UUID


class ChatCreate(ChatBase):
    pass


class ChatUpdate(ChatBase):
    id: int
    name: str
    owner_id: uuid.UUID


class Chat(ChatBase):
    id: int
    name: str
    owner_id: uuid.UUID
    created_at: datetime.datetime
