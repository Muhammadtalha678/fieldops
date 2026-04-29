from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING

from sqlalchemy import VARCHAR, Column, Boolean
from sqlmodel import Relationship, SQLModel,Field

from models.base_model import TimestampMixin
from models.job_model import Status
if TYPE_CHECKING:
    from models.job_model import Job
    from models.user_model import User
     

class JobHistory(TimestampMixin,table=True):
    __tablename__ = "job_history"  # Explicit table name
    id: int | None  = Field(default=None,primary_key=True)
    job_id: int = Field(foreign_key="jobs.id",description="Foreign key linking to the job")
    new_status:Status = Field(nullable=False)
    old_status:Status = Field(nullable=False)
    changed_by:int = Field(foreign_key="users.id")
    
    job:"Job" = Relationship(back_populates="history",
    sa_relationship_kwargs={"foreign_keys": "[JobHistory.job_id]"})
    
    user:"User" = Relationship(back_populates="history_actions",
    sa_relationship_kwargs={"foreign_keys": "[JobHistory.changed_by]"})
