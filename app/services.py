from sqlalchemy.orm import Session

from app.models import Employee


def get_all_employees(
    db: Session,
    skip: int = 0,
    limit: int = 10,
    department: str = None,
    designation: str = None,
    sort_by: str = "id",
    order: str = "asc"
):
    query = db.query(Employee)

    if department:
        query = query.filter(
            Employee.department.ilike(f"%{department}%")
        )

    if designation:
        query = query.filter(
            Employee.designation.ilike(f"%{designation}%")
        )

    allowed_sort_fields = {
        "id": Employee.id,
        "name": Employee.name,
        "email": Employee.email,
        "department": Employee.department,
        "designation": Employee.designation
    }

    sort_column = allowed_sort_fields.get(sort_by)

    if sort_column is None:
        return None

    if order.lower() == "desc":
        query = query.order_by(sort_column.desc())
    else:
        query = query.order_by(sort_column.asc())

    return (
        query
        .offset(skip)
        .limit(limit)
        .all()
    )


def search_employees(
    db: Session,
    name: str = None,
    department: str = None,
    designation: str = None
):
    query = db.query(Employee)

    if name:
        query = query.filter(
            Employee.name.ilike(f"%{name}%")
        )

    if department:
        query = query.filter(
            Employee.department.ilike(f"%{department}%")
        )

    if designation:
        query = query.filter(
            Employee.designation.ilike(f"%{designation}%")
        )

    return query.all()


def get_employee_by_id(
    db: Session,
    employee_id: int
):
    return (
        db.query(Employee)
        .filter(Employee.id == employee_id)
        .first()
    )


def create_employee(
    db: Session,
    name: str,
    email: str,
    department: str,
    designation: str
):
    new_employee = Employee(
        name=name,
        email=email,
        department=department,
        designation=designation
    )

    db.add(new_employee)

    return new_employee


def delete_employee(
    db: Session,
    employee_id: int
):
    employee = (
        db.query(Employee)
        .filter(Employee.id == employee_id)
        .first()
    )

    if employee is None:
        return None

    db.delete(employee)

    return employee


def update_employee(
    db: Session,
    employee_id: int,
    name: str,
    email: str,
    department: str,
    designation: str
):
    employee = (
        db.query(Employee)
        .filter(Employee.id == employee_id)
        .first()
    )

    if employee is None:
        return None

    employee.name = name
    employee.email = email
    employee.department = department
    employee.designation = designation

    return employee