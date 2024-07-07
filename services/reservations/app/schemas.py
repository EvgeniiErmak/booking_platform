# booking_platform/services/reservations/app/schemas.py

from pydantic import BaseModel
from datetime import datetime


class ReservationCreate(BaseModel):
    user_id: int
    venue_id: int
    date: datetime
