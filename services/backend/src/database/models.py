from typing import Annotated, Any
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import BigInteger, MetaData, String
metadata = MetaData()

# user_table = Table(
#     "users",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("user_id", BigInteger),
#     Column("echo_mode", Boolean),
#     Column("messages", Text),
#     Column("username", String),
#     schema="tg_bot"
# )

bigint = Annotated[int, "bigint"]
str_256 = Annotated[str, 256]

class Base(DeclarativeBase):
    metadata = metadata
    __table_args__ = {"schema": "fastapi"}
    type_annotation_map = {
            str_256: String(256)
        }
    

class UserTable(Base):
    __tablename__ = "users"
    user_email:    Mapped[str] = mapped_column(nullable=False)
    user_password: Mapped[str_256] = mapped_column(nullable=False)
    username:   Mapped[str] = mapped_column(nullable=False, primary_key=True)

    
