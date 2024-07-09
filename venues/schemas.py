# booking_platform/venues/schemas.py

from pydantic import BaseModel


class VenueBase(BaseModel):
    name: str
    address: str
    capacity: int
    is_active: bool = True


class VenueCreate(VenueBase):
    pass


class VenueUpdate(VenueBase):
    pass


class Venue(VenueBase):
    id: int

    class Config:
        orm_mode = True
