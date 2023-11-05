from typing import Optional
from pydantic import BaseModel, Field


class UserIn(BaseModel):
    user_email: str
    user_password: str
    username: str

class UserOut(BaseModel):
    user_email: str
    _user_password: str
    username: str
    