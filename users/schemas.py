# booking_platform/users/schemas.py

from pydantic import BaseModel, Field


class UserBase(BaseModel):
    username: str
    email: str
    full_name: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True
