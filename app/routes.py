from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.schemas import EmployeeCreate, EmployeeResponse
from app.services import (
    get_all_employees,
    search_employees,
    get_employee_by_id,
    create_employee,
    delete_employee,
    update_employee
)


router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# Get employees with pagination, filtering and sorting
@router.get(
    "/",
    response_model=list[EmployeeResponse]
)
def get_employees(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    department: str = None,
    designation: str = None,
    sort_by: str = "id",
    order: str = "asc",
    db: Session = Depends(get_db)
):
    employees = get_all_employees(
        db=db,
        skip=skip,
        limit=limit,
        department=department,
        designation=designation,
        sort_by=sort_by,
        order=order
    )

    if employees is None:
        raise HTTPException(
            status_code=400,
            detail="Invalid sort_by field"
        )

    return employees


# Search employees
@router.get(
    "/search",
    response_model=list[EmployeeResponse]
)
def search_employees_route(
    name: str = None,
    department: str = None,
    designation: str = None,
    db: Session = Depends(get_db)
):
    employees = search_employees(
        db=db,
        name=name,
        department=department,
        designation=designation
    )

    return employees


# Get employee by ID
@router.get(
    "/{employee_id}",
    response_model=EmployeeResponse
)
def get_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    employee = get_employee_by_id(
        db=db,
        employee_id=employee_id
    )

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee


# Create employee
@router.post(
    "/",
    response_model=EmployeeResponse,
    status_code=status.HTTP_201_CREATED
)
def create_employee_route(
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):
    new_employee = create_employee(
        db=db,
        name=employee.name,
        email=employee.email,
        department=employee.department,
        designation=employee.designation
    )

    try:
        db.commit()
        db.refresh(new_employee)

    except IntegrityError:
        db.rollback()

        raise HTTPException(
            status_code=409,
            detail="Email already registered"
        )

    return new_employee


# Update employee
@router.put(
    "/{employee_id}",
    response_model=EmployeeResponse
)
def update_employee_route(
    employee_id: int,
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):
    existing_employee = update_employee(
        db=db,
        employee_id=employee_id,
        name=employee.name,
        email=employee.email,
        department=employee.department,
        designation=employee.designation
    )

    if existing_employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    try:
        db.commit()
        db.refresh(existing_employee)

    except IntegrityError:
        db.rollback()

        raise HTTPException(
            status_code=409,
            detail="Email already registered"
        )

    return existing_employee


# Delete employee
@router.delete("/{employee_id}")
def delete_employee_route(
    employee_id: int,
    db: Session = Depends(get_db)
):
    employee = delete_employee(
        db=db,
        employee_id=employee_id
    )

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    db.commit()

    return {
        "message": "Employee deleted successfully"
    }