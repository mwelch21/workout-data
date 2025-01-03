from typing import List, Optional
from sqlalchemy import String, ForeignKey, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class BaseTable(DeclarativeBase):
    base_string_length: int = 250
    pass


class Tags(BaseTable):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(BaseTable.base_string_length))


class Workouts(BaseTable):
    __tablename__ = "workouts"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(BaseTable.base_string_length))
    tag: Mapped[str] = mapped_column(ForeignKey("tags.name"))
    verified: Mapped[bool] = mapped_column(Boolean)
    