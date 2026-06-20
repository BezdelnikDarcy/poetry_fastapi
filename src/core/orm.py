from datetime import datetime
from typing import Optional, Annotated
from sqlalchemy import String, text
from sqlalchemy.orm import mapped_column, DeclarativeBase, Mapped

primary_int = Annotated[int,mapped_column(primary_key=True)]
str_64_nullable = Annotated[str,mapped_column(String(64),nullable=True)]
str_64_not_nullable = Annotated[str,mapped_column(String(64))]
str_64_not_nullable_unique = Annotated[str,mapped_column(String(64), unique=True)]
simple_int_nullable = Annotated[Optional[int],mapped_column(nullable=True)]
created_at = Annotated[
    datetime,
    mapped_column(server_default=text("TIMEZONE('utc', now())")),
]
updated_at = Annotated[
    datetime,
    mapped_column(server_default=text("TIMEZONE('utc', now())")),
]


class Base(DeclarativeBase):
    created_at = Mapped[created_at]
    updated_at = Mapped[updated_at]
