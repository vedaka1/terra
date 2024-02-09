from typing import Annotated
from sqlalchemy import  MetaData, String
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from .config import settings


engine = create_async_engine(
    url=settings.TEST_DATABASE_URL,
    echo=True
)

bigint = Annotated[int, "bigint"]
str_256 = Annotated[str, 256]


class Base(DeclarativeBase):
    metadata = MetaData()
    __table_args__ = {"schema": "fastapi"}


async_session_factory = async_sessionmaker(engine, expire_on_commit=False)