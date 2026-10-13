from sqlalchemy import Column, DateTime, Integer, String, func
from sqlalchemy.orm import relationship
from app.db.database import Base

class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String(100), unique = True, nullable = False, index = True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable = False)
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable = False,
    )
    employees = relationship("Employee", back_populates="department")
