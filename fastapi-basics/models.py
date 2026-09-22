from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    owner_id=Column(Integer,ForeignKey("users.id"),nullable=False)
    title = Column(String, nullable=False)
    done = Column(Boolean, default=False)
    owner=relationship("User",back_populates="tasks")

class User(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True,index=True)
    username=Column(String,unique=True,nullable=False)
    email=Column(String,unique=True,nullable=False)
    tasks=relationship("Task",back_populates="owner")
