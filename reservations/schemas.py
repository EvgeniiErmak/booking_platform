# booking_platform/reservations/schemas.py

from pydantic import BaseModel
from datetime import datetime


class ReservationBase(BaseModel):
    user_id: int
    venue_id: int
    start_time: datetime
    end_time: datetime
    status: str


class ReservationCreate(ReservationBase):
    pass


class Reservation(ReservationBase):
    id: int

    class Config:
        orm_mode = True
