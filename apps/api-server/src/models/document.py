from enum import IntEnum
from typing import Literal
from sqlmodel import SQLModel, Field, Relationship
from src.models.base import IDMixin, TimestampMixin
from src.models.user import User
from sqlalchemy import JSON, Text
from pydantic import HttpUrl
from 

class Status(IntEnum):
    PENDING = 1
    COMPLETE = 2
    FAIL = 3

class Sentiment(IntEnum):
    POSITIVE = 1
    NEUTRAL = 2
    NEGATIVE = 3

class Document(SQLModel, IDMixin, TimestampMixin):
    user_id: int = Field(foreign_key="user.id")
    summary: str = Field(sa_column=Text)
    doc_location: HttpUrl = Field()
    category: str = Field()
    sentiment: Sentiment = Field()
    title: str = Field()
    # separate table is overkill
    key_points: list[str] = Field(sa_column=JSON)
    read_time_est_min: int = Field()
    word_count: int = Field()
    language_code: str = Field()
    summary_model: str | None = Field(nullable=True)
    process_status: Status = Field(default=Status.PENDING)
    embedding: bytes = Field(sa_column=)

    user: User = Relationship(back_populates="documents")