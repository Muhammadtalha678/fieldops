from typing import List, TYPE_CHECKING

from sqlmodel import Relationship, SQLModel,Field
from enum import Enum
from pydantic import EmailStr

from models.base_model import TimestampMixin

if TYPE_CHECKING:
    from models.job_model import Job
    from models.job_history_model import JobHistory
    from models.notification_model import Notification

class UserRole(str, Enum):
    ADMIN = "admin"
    CLIENT = "client"
    TECHNICIAN = "technician"
# class User(SQLModel,TimestampMixin,table=True):
#     id:int | None = Field(default=None,sa_column=Column(Integer,Identity(),primary_key=True))
#     email:str = Field(sa_column=Column(VARCHAR(255),nullable=False,unique=True))
#     password:str = Field(sa_column=Column(VARCHAR(255),nullable=False))
#     role:str = Field(sa_column= Column(VARCHAR(20),nullable=False))   
class User(TimestampMixin,table=True):
    __tablename__ = "users"
    id:int | None = Field(default=None,primary_key=True)
    email:EmailStr = Field(max_length=255,nullable=False,unique=True)
    password:str = Field(max_length=255,nullable=False)
    role: UserRole  = Field(nullable=False)

    job_as_client:List["Job"] = Relationship(back_populates="client",sa_relationship_kwargs={"foreign_keys": "[Job.client_id]"})
    job_as_tech:List["Job"] = Relationship(back_populates="technician",sa_relationship_kwargs={"foreign_keys": "[Job.tech_id]"})
    history_actions:List["JobHistory"] = Relationship(back_populates="user",sa_relationship_kwargs={"foreign_keys":"[JobHistory.changed_by]"})

    notifications:List["Notification"] = Relationship(back_populates="user",sa_relationship_kwargs={"foreign_keys":"[Notification.user_id]"})

class UserLogin(SQLModel):
    email:EmailStr
    password:str= Field(min_length=8)
    # role:UserRole 


class UserCreate(SQLModel):
    email:EmailStr
    password:str
    role: UserRole

class UserRead(SQLModel):
    id:int
    email:EmailStr
    role: UserRole

class Token(SQLModel):
    access_token:str
    user:UserRead