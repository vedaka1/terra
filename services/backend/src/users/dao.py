from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload, joinedload, aliased

from src.dao import BaseDAO
from .models import UserModel, RefreshSessionModel, user_to_user
from .schemas import UserCreateDB, UserUpdateDB, RefreshSessionCreate, RefreshSessionUpdate, FriendCreateDB, FriendUpdateDB

class UserDAO(BaseDAO[UserModel, UserCreateDB, UserUpdateDB]):
    model = UserModel


class RefreshSessionDAO(BaseDAO[RefreshSessionModel, RefreshSessionCreate, RefreshSessionUpdate]):
    model = RefreshSessionModel


class FriendDAO(BaseDAO[user_to_user, FriendCreateDB, FriendUpdateDB]):
    model = user_to_user

    @classmethod
    async def find_all_user_friends(
        cls,
        session: AsyncSession,
        user_id,
        offset: int = 0,
        limit: int = 100,
        **filter_by
    ) -> List[UserModel]:
        query = (
            select(UserModel)
            .select_from(cls.model)
            .join(UserModel, cls.model.c.friend_id == UserModel.id)
            .where(cls.model.c.user_id == user_id)
            .filter_by(**filter_by)
            .offset(offset)
            .limit(limit)
        )
        result = await session.execute(query)
        return result.scalars().all()
