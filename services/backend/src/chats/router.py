from typing import List, Optional

from fastapi import APIRouter, Depends, Request, Response, status

from src.chats.schemas import Chat, Message
from src.chats.service import ChatService, MessageService
from src.users.models import UserModel

from .dependencies import (
    get_current_active_user,
    get_current_superuser,
    get_current_user,
)

chat_router = APIRouter(prefix="/chats", tags=["Chat"])


@chat_router.post("")
async def create_chat(
    name: str, current_user: UserModel = Depends(get_current_active_user)
) -> Chat:
    return await ChatService.create_chat(name, current_user.id)


@chat_router.get("")
async def get_all_user_chats(
    offset: Optional[int] = 0,
    limit: Optional[int] = 100,
    current_user: UserModel = Depends(get_current_active_user),
) -> List[Chat]:
    return await ChatService.get_chats_list(
        user_id=current_user.id, offset=offset, limit=limit
    )


@chat_router.delete("/{chat_id}")
async def delete_chat(
    chat_id: int, current_user: UserModel = Depends(get_current_active_user)
) -> None:
    return await ChatService.delete_chat(chat_id, current_user.id)


@chat_router.post("/{chat_id}/messages")
async def send_message(
    chat_id: int,
    content: str,
    current_user: UserModel = Depends(get_current_active_user),
) -> Message:
    return await MessageService.send_message(chat_id, content, current_user.id)


@chat_router.get("/{chat_id}/messages")
async def get_chat_messages(
    chat_id: int,
    offset: Optional[int] = 0,
    limit: Optional[int] = 100,
    user: UserModel = Depends(get_current_active_user),
) -> List[Message]:
    return await MessageService.get_chat_messages_list(
        chat_id, offset=offset, limit=limit
    )
