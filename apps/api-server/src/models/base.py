from sqlmodel import SQLModel, Field
from datetime import datetime, timezone


class TimestampMixin(SQLModel):
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
    )
    updated_at: datetime | None = Field(
        nullable=True,
        sa_column_kwargs={"onupdate": datetime.now(timezone.utc)},
    )


class IDMixin(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
