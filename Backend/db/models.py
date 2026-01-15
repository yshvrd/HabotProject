from sqlalchemy import Column, String, Integer, DateTime, func
from sqlalchemy.orm import declarative_base
import uuid

# Enables SQLAlchemy to map Python classes to DB tables
Base = declarative_base() # ORM base model


# Create table
class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    department = Column(String, nullable=True)
    role = Column(String, nullable=True)
    date_joined = Column(DateTime(timezone=True), server_default=func.now())

    