from typing import Annotated

from sqlalchemy import Enum
from sqlalchemy.orm import mapped_column

from src.account.constants import UserSexEnum, UserStatusEnum
from sqlalchemy.orm import Mapped
from src.core.orm import (
    primary_int,
    str_64_nullable,
    str_64_not_nullable,
    simple_int_nullable,
    str_64_not_nullable_unique,
    Base
)



class User(Base):
    __tablename__ = "users"
    id: Mapped[primary_int]
    email: Mapped[str_64_not_nullable_unique]
    username: Mapped[str_64_nullable]
    password: Mapped[str_64_nullable]
    name: Mapped[str_64_nullable]
    fullname: Mapped[str_64_nullable]
    age: Mapped[simple_int_nullable]
    sex: Mapped[UserSexEnum] = mapped_column(
        Enum(UserSexEnum),
        nullable=False,
    )
    status: Mapped[UserStatusEnum] = mapped_column(
        Enum(UserStatusEnum),
        nullable=False,
    )

