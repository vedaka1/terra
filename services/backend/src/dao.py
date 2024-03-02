from typing import Any, Dict, Generic, List, Optional, TypeVar, Union

from pydantic import BaseModel
from sqlalchemy import delete, insert, select, update
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import func

from src.database import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class BaseDAO(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    model = None

    @classmethod
    async def find_one_or_none(
        cls, session: AsyncSession, *filter, **filter_by
    ) -> Optional[ModelType]:
        query = select(cls.model).filter(*filter).filter_by(**filter_by)
        result = await session.execute(query)
        return result.scalars().one_or_none()

    @classmethod
    async def find_all(
        cls,
        session: AsyncSession,
        *filter,
        offset: int = 0,
        limit: int = 100,
        **filter_by,
    ) -> List[ModelType]:
        query = (
            select(cls.model)
            .filter(*filter)
            .filter_by(**filter_by)
            .offset(offset)
            .limit(limit)
        )
        result = await session.execute(query)
        return result.scalars().all()

    @classmethod
    async def add(
        cls, session: AsyncSession, obj_in: Union[CreateSchemaType, Dict[str, Any]]
    ) -> Optional[ModelType]:
        if isinstance(obj_in, dict):
            create_data = obj_in
        else:
            create_data = obj_in.model_dump(exclude_unset=True)
        try:
            query = insert(cls.model).values(**create_data).returning(cls.model)
            result = await session.execute(query)
            return result.scalars().first()
        except (SQLAlchemyError, Exception) as e:
            if isinstance(e, SQLAlchemyError):
                msg = "Database Exc: Cannot insert data into table"
            elif isinstance(e, Exception):
                msg = "Unknown Exc: Cannot insert data into table"
            print(msg)
            return None

    @classmethod
    async def delete(cls, session: AsyncSession, *filter, **filter_by) -> None:
        query = delete(cls.model).filter(*filter).filter_by(**filter_by)
        await session.execute(query)

    @classmethod
    async def update(
        cls,
        session: AsyncSession,
        *where,
        obj_in: Union[UpdateSchemaType, Dict[str, Any]],
    ) -> Optional[ModelType]:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)

        query = (
            update(cls.model)
            .
            # where(cls.model.id == id).
            where(*where)
            .values(**update_data)
            .returning(cls.model)
        )
        result = await session.execute(query)
        return result.scalars().one()

    @classmethod
    async def count(cls, session: AsyncSession, *filter, **filter_by):
        query = (
            select(func.count())
            .select_from(cls.model)
            .filter(*filter)
            .filter_by(**filter_by)
        )
        result = await session.execute(query)
        return result.scalar()
