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
def get_employee_by_id(db: Session, employee_id: int) -> Employee | None:
    result = db.query(Employee).filter(Employee.id == employee_id).first()
    
    return result 

# get all employees and pagination logic
def get_employees(db: Session, page: int = 1, department: str | None = None, role: str | None = None,):
    query = db.query(Employee)

    # search by department
    if department:
        query = query.filter(Employee.department == department)
    # search by role
    if role:
        query = query.filter(Employee.role == role)

    limit = 10 # max per page
    offset = (page - 1) * limit # page logic (no. of db rows to skip)
    result = query.offset(offset).limit(limit).all()

    return result 




# Update employee

