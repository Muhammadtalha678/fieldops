

from datetime import datetime

from sqlmodel import Field, SQLModel


class TimestampMixin(SQLModel):
    """
    Mixin for adding timestamp fields to models.

    Provides created_at and updated_at fields for tracking
    record creation and modification times.
    """
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(),
        nullable=False,
        description="Timestamp when record was created",
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(),
        nullable=False,
        description="Timestamp when record was last updated",
    )