from src.dao import BaseDAO

from .models import ChatModel, MessageModel
from .schemas import ChatCreate, ChatUpdate, MessageCreate, MessageUpdate


class MessageDAO(BaseDAO[MessageModel, MessageCreate, MessageUpdate]):
    model = MessageModel


class ChatDAO(BaseDAO[ChatModel, ChatCreate, ChatUpdate]):
    model = ChatModel
