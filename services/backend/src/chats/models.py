import uuid
from datetime import datetime
from typing import List

import sqlalchemy as sa
from fastapi import FastAPI
from sqlalchemy import Column, ForeignKey, Integer, Table, false
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from src.database import Base

# message_to_chat = Table(
#     "message_to_chat",
#     Base.metadata,
#     Column("message_id", Integer, ForeignKey("fastapi.message.id")),
#     Column("chat_id", Integer, ForeignKey("fastapi.chat.id")),
#     schema="fastapi",
# )


user_to_chat = Table(
    "user_to_chat",
    Base.metadata,
    Column("user_id", UUID, ForeignKey("user.id")),
    Column("chat_id", Integer, ForeignKey("chat.id")),
)


class ChatModel(Base):
    __tablename__ = "chat"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(nullable=False)
    owner_id: Mapped[uuid.UUID] = mapped_column(
        sa.ForeignKey(f"user.id", ondelete="CASCADE")
    )
    created_at: Mapped[datetime] = mapped_column(
        sa.TIMESTAMP(timezone=True), server_default=func.now()
    )


class MessageModel(Base):
    __tablename__ = "message"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    chat_id: Mapped[int] = mapped_column(sa.ForeignKey(f"chat.id", ondelete="CASCADE"))
    user_id: Mapped[uuid.UUID] = mapped_column(
        sa.ForeignKey(f"user.id", ondelete="CASCADE")
    )
    created_at: Mapped[datetime] = mapped_column(
        sa.TIMESTAMP(timezone=True), server_default=func.now()
    )
    content: Mapped[str] = mapped_column(nullable=False)
