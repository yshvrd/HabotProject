from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from db.models import Employee
from core.schemas import CreateEmployee


# create employee
def create_employee(db: Session, employee_in: CreateEmployee) -> Employee:
    employee = Employee(
        name=employee_in.name,
        email=employee_in.email,
        department=employee_in.department,
        role=employee_in.role,
    )

    db.add(employee)

    try:
        db.commit()
        db.refresh(employee)
    except IntegrityError:
        db.rollback()
        raise

    return employee




# get employee by id 

