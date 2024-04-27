from typing import Annotated

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from .config import settings

engine = create_async_engine(url=settings.DB_URL, echo=False)


class Base(DeclarativeBase):
    metadata = MetaData()


async_session_factory = async_sessionmaker(engine, expire_on_commit=False)
