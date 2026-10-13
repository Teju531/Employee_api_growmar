import uuid

import pytest
from sqlalchemy.exc import IntegrityError

from app.db.database import SessionLocal
from app.models import Department, Employee


def test_duplicate_employee_work_email_is_rejected():
    unique_id = uuid.uuid4().hex
    email = f"employee-{unique_id}@example.com"

    with SessionLocal() as db:
        try:
            # Create a department for the employees
            department = Department(name=f"Test Department {unique_id}")
            db.add(department)
            db.flush()

            # Insert the first employee
            employee1 = Employee(
                name="First Employee",
                work_email=email,
                department_id=department.id,
            )
            db.add(employee1)
            db.flush()

            # Try inserting another employee with the same email
            employee2 = Employee(
                name="Second Employee",
                work_email=email,
                department_id=department.id,
            )
            db.add(employee2)

            # The database must reject the duplicate email
            with pytest.raises(IntegrityError):
                db.flush()

        finally:
            # Undo test changes, including the first employee
            db.rollback()


def test_employee_can_have_a_manager():
    unique_id = uuid.uuid4().hex

    with SessionLocal() as db:
        try:
            department = Department(name=f"Manager Test {unique_id}")
            db.add(department)
            db.flush()

            manager = Employee(
                name="Team Manager",
                work_email=f"manager-{unique_id}@example.com",
                department_id=department.id,
            )
            db.add(manager)
            db.flush()

            employee = Employee(
                name="Team Member",
                work_email=f"member-{unique_id}@example.com",
                department_id=department.id,
                manager_id=manager.id,
            )
            db.add(employee)
            db.flush()

            db.refresh(employee)

            assert employee.manager_id == manager.id
            assert employee.manager.name == "Team Manager"
            assert employee in manager.team_members

        finally:
            db.rollback()

def test_employee_cannot_be_their_own_manager():
    unique_id = uuid.uuid4().hex

    with SessionLocal() as db:
        try:
            department = Department(name=f"Self Manager Test {unique_id}")
            db.add(department)
            db.flush()

            employee = Employee(
                name="Self Managed Employee",
                work_email=f"self-{unique_id}@example.com",
                department_id=department.id,
            )
            db.add(employee)
            db.flush()

            # An employee cannot be their own manager
            employee.manager_id = employee.id

            with pytest.raises(IntegrityError):
                db.flush()

        finally:
            db.rollback()
