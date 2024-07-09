# booking_platform/venues/models.py

from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class Venue(Base):
    __tablename__ = "venues"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String, index=True)
    capacity = Column(Integer)
    is_active = Column(Boolean, default=True)
