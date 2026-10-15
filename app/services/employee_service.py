from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Employee

#addding the Employee data to database
def create_employee(db: Session, employee_data: dict) -> Employee:
    employee = Employee(**employee_data)
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee

#gets employee data
def get_employee(db: Session, employee_id: int) -> Employee | None:
    return db.get(Employee, employee_id)

#filtering + pagination + search
def list_employees(
    db: Session,
    page: int = 1,
    size: int = 20,
    department_id: int | None = None,
    q: str | None = None,
):
    query = select(Employee).where(Employee.is_active.is_(True))

    if department_id is not None:
        query = query.where(Employee.department_id == department_id)

    if q:
        query = query.where(Employee.name.ilike(f"%{q.strip()}%"))

    total = db.scalar(
        select(__import__("sqlalchemy").func.count()).select_from(query.subquery())
    )

    employees = db.scalars(
        query.order_by(Employee.id)
        .offset((page - 1) * size)
        .limit(size)
    ).all()

    return {"items": employees, "total": total or 0, "page": page, "size": size}


def update_employee(
    db: Session,
    employee: Employee,
    changes: dict,
) -> Employee:
    for field, value in changes.items():
        setattr(employee, field, value)

    db.commit()
    db.refresh(employee)
    return employee


def soft_delete_employee(db: Session, employee: Employee) -> None:
    employee.is_active = False
    db.commit()
