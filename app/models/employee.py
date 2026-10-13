from sqlalchemy import (
    Boolean,
    CheckConstraint,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    func,
)
from sqlalchemy.orm import relationship

from app.db.database import Base


class Employee(Base):
    __tablename__ = "employees"

    __table_args__ = (
        CheckConstraint(
            "manager_id IS NULL OR manager_id != id",
            name="ck_employee_not_own_manager",
        ),
    )

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, index=True)
    work_email = Column(String(255), nullable=False, unique=True)
    department_id = Column(
        Integer,
        ForeignKey("departments.id"),
        nullable=False,
        index=True,
    )
    manager_id = Column(
        Integer,
        ForeignKey("employees.id"),
        nullable=True,
        index=True,
    )
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
    is_active = Column(Boolean, nullable=False, default=True, server_default="true")

    department = relationship("Department", back_populates="employees")
    manager = relationship(
        "Employee",
        remote_side="Employee.id",
        back_populates="team_members",
    )
    team_members = relationship("Employee", back_populates="manager")
    employee_roles = relationship("EmployeeRole", back_populates="employee")
