from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING

from sqlalchemy import VARCHAR, Column, Boolean
from sqlmodel import Relationship, SQLModel,Field

from models.base_model import TimestampMixin

if TYPE_CHECKING:
    from models.user_model import User

     

class Notification(TimestampMixin,table=True):
    id: int | None  = Field(default=None,primary_key=True)
    user_id: int = Field(foreign_key="users.id",description="Foreign key linking to the user according to the status if job completed than admin notify if admin assign job than technician and client notify")
    message:str = Field(nullable=False)
    is_read: bool = Field(default=False)

    user:"User" = Relationship(back_populates="notifications",
    sa_relationship_kwargs={"foreign_keys": "[Notification.user_id]"})
    __tablename__ = "notifications"  # Explicit table name