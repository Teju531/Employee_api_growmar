from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Department


def create_department(db: Session, name: str) -> Department:
    department = Department(name=name)
    db.add(department)
    db.commit()
    db.refresh(department)
    return department


def get_department(db: Session, department_id: int) -> Department | None:
    return db.get(Department, department_id)


def list_departments(db: Session) -> list[Department]:
    query = select(Department).order_by(Department.id)
    return list(db.scalars(query).all())
