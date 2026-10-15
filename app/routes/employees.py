from fastapi import APIRouter, Depends, HTTPException, Query, Response, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models import Department, Employee
from app.schemas.employee import (
    EmployeeCreate,
    EmployeeResponse,
    EmployeeUpdate,
)
from app.services import employee_service

router = APIRouter(prefix="/employees", tags=["Employees"])


@router.post(
    "",
    response_model=EmployeeResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_employee(
    data: EmployeeCreate,
    db: Session = Depends(get_db),
):
    if not db.get(Department, data.department_id):
        raise HTTPException(
            status_code=404,
            detail={"error": "Department not found"},
        )

    if data.manager_id is not None and not db.get(Employee, data.manager_id):
        raise HTTPException(
            status_code=404,
            detail={"error": "Manager not found"},
        )

    try:
        return employee_service.create_employee(
            db,
            data.model_dump(),
        )
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail={"error": "Employee email already exists or data conflicts"},
        )


@router.get("")
def list_employees(
    page: int = Query(1, ge=1),
    size: int = Query(20, ge=1, le=100),
    department: int | None = Query(None, gt=0),
    q: str | None = Query(None, max_length=100),
    db: Session = Depends(get_db),
):
    result = employee_service.list_employees(
        db,
        page=page,
        size=size,
        department_id=department,
        q=q,
    )

    return {
        "items": result["items"],
        "total": result["total"],
        "page": result["page"],
        "size": result["size"],
    }


@router.get("/{employee_id}", response_model=EmployeeResponse)
def get_employee(
    employee_id: int,
    db: Session = Depends(get_db),
):
    employee = employee_service.get_employee(db, employee_id)

    if not employee or not employee.is_active:
        raise HTTPException(
            status_code=404,
            detail={"error": "Employee not found"},
        )

    return employee


@router.patch("/{employee_id}", response_model=EmployeeResponse)
def update_employee(
    employee_id: int,
    data: EmployeeUpdate,
    db: Session = Depends(get_db),
):
    employee = employee_service.get_employee(db, employee_id)

    if not employee or not employee.is_active:
        raise HTTPException(
            status_code=404,
            detail={"error": "Employee not found"},
        )

    changes = data.model_dump(exclude_unset=True)

    if "department_id" in changes and changes["department_id"] is not None:
        if not db.get(Department, changes["department_id"]):
            raise HTTPException(
                status_code=404,
                detail={"error": "Department not found"},
            )

    if "manager_id" in changes and changes["manager_id"] is not None:
        if changes["manager_id"] == employee_id:
            raise HTTPException(
                status_code=422,
                detail={"error": "An employee cannot be their own manager"},
            )

        if not db.get(Employee, changes["manager_id"]):
            raise HTTPException(
                status_code=404,
                detail={"error": "Manager not found"},
            )

    try:
        return employee_service.update_employee(db, employee, changes)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail={"error": "Employee email already exists or data conflicts"},
        )


@router.delete("/{employee_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db),
):
    employee = employee_service.get_employee(db, employee_id)

    if not employee or not employee.is_active:
        raise HTTPException(
            status_code=404,
            detail={"error": "Employee not found"},
        )

    employee_service.soft_delete_employee(db, employee)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
