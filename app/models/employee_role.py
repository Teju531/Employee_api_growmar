from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.db.database import Base


class EmployeeRole(Base):
    __tablename__ = "employee_roles"

    employee_id = Column(
        Integer,
        ForeignKey("employees.id", ondelete="CASCADE"),
        primary_key=True,
    )
    role_id = Column(
        Integer,
        ForeignKey("roles.id", ondelete="CASCADE"),
        primary_key=True,
    )

    employee = relationship("Employee", back_populates="employee_roles")
    role = relationship("Role", back_populates="employee_roles")
