from datetime import datetime
from enum import Enum
from typing import List, TYPE_CHECKING

from sqlalchemy import VARCHAR, Column,Integer,Identity,ForeignKey
from sqlmodel import Relationship, SQLModel,Field

from models.base_model import TimestampMixin
if TYPE_CHECKING:
    from models.job_history_model import JobHistory
    from models.user_model import User
    
class Status(str,Enum):
    PENDING = "pending" 
    ASSIGNED = "assigned" 
    IN_PROGRESS = "in_progress" 
    COMPLETED = "completed" 
    CANCELLED = "cancelled"
     
     

class Job(TimestampMixin,table=True):
    __tablename__ = "jobs"  # Explicit table name

    id: int | None  = Field(default=None,primary_key=True)
    
    title:str = Field(max_length=255,nullable=False,
    description="The heading or title of the job")

    description:str | None= Field(description="The description of the job")
    
    status:Status = Field(default=Status.PENDING,nullable=False)
    
    client_id: int = Field(foreign_key="users.id",nullable=False,
    description="Foreign key linking to the user whose role is client")
    
    tech_id: int = Field(foreign_key="users.id",
    description="Foreign key linking to the user whose role is technician",
    nullable=False)
    
    sheduled_at: datetime = Field(nullable=False)

    client:"User" = Relationship(back_populates="job_as_client",sa_relationship_kwargs={"foreign_keys": "[Job.client_id]"})
    technician:"User" = Relationship(back_populates="job_as_tech",sa_relationship_kwargs={"foreign_keys": "[Job.tech_id]"})
    
    history:List["JobHistory"] = Relationship(back_populates="job")

class JobCreate(SQLModel):
    title:str = Field(max_length=255)

    description:str | None = None
    
    status:Status = Field(default=Status.PENDING)
    
    client_id: int 
    
    tech_id: int 
    
    sheduled_at: datetime
    