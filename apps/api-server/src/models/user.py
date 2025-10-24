from sqlmodel import SQLModel, Field
from .base import IDMixin, TimestampMixin
from pydantic import EmailStr


class User(IDMixin, TimestampMixin, SQLModel, table=True):
    email: EmailStr = Field(index=True, unique=True)
    auth_manager_id: str | None = Field(nullable=True)
