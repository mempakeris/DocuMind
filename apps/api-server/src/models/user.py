from sqlmodel import SQLModel, Field
from pydantic import EmailStr, UUID4
from uuid import uuid4

from src.models.base import BaseModel


class User(BaseModel, SQLModel, table=True):
    account_id: UUID4 = Field(index=True, unique=True, default_factory=uuid4)
    email: EmailStr = Field(index=True, unique=True)
    auth_manager_id: str | None = Field(nullable=True)
