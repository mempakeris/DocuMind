from sqlalchemy import TIMESTAMP, Column
from sqlmodel import SQLModel, Field
from datetime import datetime, timezone


class BaseModel(SQLModel, table=False):
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column_kwargs={
            'nullable': True,
        },
        sa_type=TIMESTAMP(timezone=True),
    )
    updated_at: datetime | None = Field(
        sa_column_kwargs={
            'nullable': True,
            'onupdate': lambda: datetime.now(timezone.utc)
        },
        sa_type=TIMESTAMP(timezone=True),
    )
    id: int | None = Field(default=None, primary_key=True)
