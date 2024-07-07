# booking_platform/services/venues/app/schemas.py

from pydantic import BaseModel


class VenueCreate(BaseModel):
    name: str
    location: str


class VenueResponse(BaseModel):
    id: int
    name: str
    location: str

    class Config:
        from_attributes = True  # Pydantic V2
