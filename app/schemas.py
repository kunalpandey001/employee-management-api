from pydantic import BaseModel, ConfigDict, EmailStr, Field


class EmployeeCreate(BaseModel):
    name: str = Field(
        ...,
        min_length=2,
        max_length=100
    )

    email: EmailStr

    department: str = Field(
        ...,
        min_length=2,
        max_length=100
    )

    designation: str = Field(
        ...,
        min_length=2,
        max_length=100
    )


class EmployeeResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    department: str
    designation: str

    model_config = ConfigDict(from_attributes=True)

class EmployeeListResponse(BaseModel):
    items: list[EmployeeResponse]
    total: int
    skip: int
    limit: int