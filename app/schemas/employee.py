from datetime import date, datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field, model_validator


class EmployeeCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    work_email: EmailStr
    department_id: int = Field(gt=0)
    manager_id: int | None = Field(default=None, gt=0)
    joining_date: date | None = None

    @model_validator(mode="after")
    def validate_name(self):
        if not self.name.strip():
            raise ValueError("Name cannot be empty")
        return self

    @model_validator(mode="after")
    def validate_joining_date(self):
        if self.joining_date and self.joining_date > date.today():
            raise ValueError("Joining date cannot be in the future")
        return self


class EmployeeUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=100)
    work_email: EmailStr | None = None
    department_id: int | None = Field(default=None, gt=0)
    manager_id: int | None = Field(default=None, gt=0)
    joining_date: date | None = None

    @model_validator(mode="after")
    def validate_fields(self):
        if self.name is not None and not self.name.strip():
            raise ValueError("Name cannot be empty")

        if self.joining_date and self.joining_date > date.today():
            raise ValueError("Joining date cannot be in the future")

        return self


class EmployeeResponse(BaseModel):
    id: int
    name: str
    work_email: str
    department_id: int
    manager_id: int | None
    joining_date: date | None = None
    created_at: datetime
    updated_at: datetime
    is_active: bool

    model_config = ConfigDict(from_attributes=True)
