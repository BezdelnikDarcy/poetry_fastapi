from datetime import datetime

from pydantic import BaseModel

from src.account.constants import UserSexEnum, UserStatusEnum


class UserCreateSchema(BaseModel):
    email: str
    sex: UserSexEnum
    status: UserStatusEnum



class UserResponseSchema(BaseModel):
    id: int
    username: str | None = None
    email: str
    sex: UserSexEnum
    status: UserStatusEnum
    name: str | None = None
    age: int | None = None
    created_at: datetime
    updated_at: datetime