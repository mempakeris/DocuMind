from enum import IntEnum
from sqlmodel import SQLModel, Field, Relationship
from src.models.base import BaseModel
from src.models.user import User
from sqlalchemy import ARRAY, Text, String, Column
from pydantic import HttpUrl
from pgvector.sqlalchemy import Vector


class Status(IntEnum):
    PENDING = 1
    COMPLETE = 2
    FAIL = 3


class Sentiment(IntEnum):
    POSITIVE = 1
    NEUTRAL = 2
    NEGATIVE = 3


class Document(BaseModel, SQLModel, table=True):
    user_id: int = Field(foreign_key="user.id")
    summary: str | None = Field(sa_column=Text)
    doc_location: str = Field()
    category: str | None = Field(nullable=True)
    sentiment: Sentiment | None = Field(nullable=True)
    title: str | None = Field(nullable=True)
    # separate table is overkill
    key_points: list[str] | None = Field(sa_column=Column(ARRAY(String)))
    read_time_est_min: int | None = Field(nullable=True)
    word_count: int | None = Field(nullable=True)
    language_code: str | None = Field(nullable=True)
    summary_model: str | None = Field(nullable=True)
    process_status: Status = Field(default=Status.PENDING)
    embedding: bytes | None = Field(sa_column=Vector)

    user: User = Relationship()
