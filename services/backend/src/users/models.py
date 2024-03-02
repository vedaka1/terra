import uuid
from datetime import datetime
from typing import List

import sqlalchemy as sa
from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from src.database import Base

user_to_user = Table(
    "user_to_user",
    Base.metadata,
    Column("user_id", UUID, ForeignKey("fastapi.user.id")),
    Column("friend_id", UUID, ForeignKey("fastapi.user.id")),
    schema="fastapi",
)


class UserModel(Base):
    __tablename__ = "user"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID,
        primary_key=True,
        index=True,
        default=uuid.uuid4,
    )
    email: Mapped[str] = mapped_column(nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    username: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True)
    is_verified: Mapped[bool] = mapped_column(default=False)
    is_superuser: Mapped[bool] = mapped_column(default=False)

    users: Mapped[List["UserModel"]] = relationship(
        "UserModel",
        secondary=user_to_user,
        primaryjoin=id == user_to_user.c.user_id,
        secondaryjoin=id == user_to_user.c.friend_id,
        back_populates="friends",
    )
    friends: Mapped[List["UserModel"]] = relationship(
        "UserModel",
        secondary=user_to_user,
        primaryjoin=id == user_to_user.c.friend_id,
        secondaryjoin=id == user_to_user.c.user_id,
        back_populates="users",
    )


class RefreshSessionModel(Base):
    __tablename__ = "refresh_session"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    refresh_token: Mapped[uuid.UUID] = mapped_column(UUID, index=True)
    expires_in: Mapped[int]
    created_at: Mapped[datetime] = mapped_column(
        sa.TIMESTAMP(timezone=True), server_default=func.now()
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        sa.ForeignKey(f"fastapi.user.id", ondelete="CASCADE")
    )
