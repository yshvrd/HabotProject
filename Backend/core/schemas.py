from pydantic import BaseModel, EmailStr, Field
from datetime import datetime


# pydantic model for creating an employee (POST)
class CreateEmployee(BaseModel):
    name: str = Field(..., min_length=1)
    email: EmailStr
    department: str | None = None
    role: str | None = None


# pydantic model for Update an employee (PUT)
class UpdateEmployee(BaseModel):
    name: str | None = Field(None, min_length=1)
    email: EmailStr | None = None
    department: str | None = None
    role: str | None = None


# pydantic model for response from db (GET)
class EmployeeResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    department: str | None
    role: str | None
    date_joined: datetime

    class Config:    # allows Pydantic to serialize SQLAlchemy ORM objects safely as API responses
        from_attributes = True





