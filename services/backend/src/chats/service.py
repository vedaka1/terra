import uuid
from datetime import datetime, timedelta, timezone
from typing import List, Optional

from fastapi import HTTPException, status

from src.config import settings
from src.database import async_session_factory
from src.exceptions import InvalidTokenException, TokenExpiredException

from .dao import ChatDAO, MessageDAO
from .models import ChatModel, MessageModel
from .schemas import ChatCreate, Message, MessageCreate


class ChatService:
    @classmethod
    async def create_chat(cls, name: str, user_id: uuid.UUID) -> ChatModel:
        async with async_session_factory() as session:
            chat = await ChatDAO.add(session, ChatCreate(name=name, owner_id=user_id))
            await session.commit()
        return chat

    @classmethod
    async def delete_chat(cls, id: int, user_id: uuid.UUID) -> ChatModel:
        async with async_session_factory() as session:
            chat = await ChatDAO.delete(session, owner_id=user_id, id=id)
            await session.commit()
        return chat

    @classmethod
    async def get_chats_list(
        cls, user_id: uuid.UUID, offset: int = 0, limit: int = 100, **filter_by
    ) -> List[ChatModel]:
        async with async_session_factory() as session:
            chats = await ChatDAO.find_all(
                session, owner_id=user_id, offset=offset, limit=limit, **filter_by
            )
        if chats is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Users not found"
            )
        return chats


class MessageService:
    @classmethod
    async def send_message(
        cls, chat_id: int, content: str, user_id: uuid.UUID
    ) -> MessageModel:
        async with async_session_factory() as session:
            message = await MessageDAO.add(
                session,
                MessageCreate(chat_id=chat_id, user_id=user_id, content=content),
            )
            await session.commit()
        return message

    @classmethod
    async def get_chat_messages_list(
        cls, chat_id: int, offset: int = 0, limit: int = 100, **filter_by
    ) -> List[Message]:
        async with async_session_factory() as session:
            messages = await MessageDAO.find_all(
                session, chat_id=chat_id, offset=offset, limit=limit, **filter_by
            )
            return messages
