# booking_platform/venues/utils.py

from sqlalchemy.orm import Session
from venues import models, schemas


def get_venue(db: Session, venue_id: int):
    return db.query(models.Venue).filter(models.Venue.id == venue_id).first()


def get_venue_by_name(db: Session, name: str):
    return db.query(models.Venue).filter(models.Venue.name == name).first()


def create_venue(db: Session, venue: schemas.VenueCreate):
    db_venue = models.Venue(**venue.dict())
    db.add(db_venue)
    db.commit()
    db.refresh(db_venue)
    return db_venue
