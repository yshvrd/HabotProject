from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.session import get_db

from core.employee_crud import (
    create_employee,
    get_employee_by_id,
    get_employees,
    update_employee,
    delete_employee,
)
from core.schemas import (
    CreateEmployee,
    UpdateEmployee,
    EmployeeResponse,
)

from core.auth import get_current_user



router = APIRouter(prefix="/api/employees", tags=["employees"])


# create employee endpoint 
@router.post("/", response_model=EmployeeResponse, status_code=status.HTTP_201_CREATED,)
def create_employee_api(employee_in: CreateEmployee, db: Session = Depends(get_db), _: str = Depends(get_current_user)):
    try:
        return create_employee(db, employee_in)
    
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Employee with this email already exists",
        )



# get employee by id endpoint 
@router.get("/{employee_id}", response_model=EmployeeResponse)
def get_employee_api(employee_id: int, db: Session = Depends(get_db), _: str = Depends(get_current_user)):
    employee = get_employee_by_id(db, employee_id)

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    return employee

# list employees endpoint 
@router.get("/", response_model=list[EmployeeResponse])
def list_employees_api(page: int = 1, department: str | None = None, role: str | None = None, db: Session = Depends(get_db), _: str = Depends(get_current_user)):
    return get_employees(db, page, department, role)



# Update employee endpoint 
@router.put("/{employee_id}", response_model=EmployeeResponse)
def update_employee_api(employee_id: int, employee_in: UpdateEmployee, db: Session = Depends(get_db), _: str = Depends(get_current_user)):
    employee = update_employee(db, employee_id, employee_in)

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    return employee



# delete employee endpoint 
@router.delete("/{employee_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_employee_api(employee_id: int, db: Session = Depends(get_db), _: str = Depends(get_current_user)):
    success = delete_employee(db, employee_id)

    if not success:
        raise HTTPException(status_code=404, detail="Employee not found")




