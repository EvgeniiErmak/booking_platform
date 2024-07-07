# booking_platform/services/venues/app/routers/venue_router.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, utils

router = APIRouter()


@router.post("/venues/", response_model=schemas.VenueResponse)
def create_venue(venue: schemas.VenueCreate, db: Session = Depends(utils.get_db)):
    db_venue = db.query(models.Venue).filter(models.Venue.name == venue.name).first()
    if db_venue:
        raise HTTPException(status_code=400, detail="Venue already registered")
    new_venue = models.Venue(**venue.dict())
    db.add(new_venue)
    db.commit()
    db.refresh(new_venue)
    return new_venue


@router.get("/venues/{venue_id}", response_model=schemas.VenueResponse)
def read_venue(venue_id: int, db: Session = Depends(utils.get_db)):
    venue = db.query(models.Venue).filter(models.Venue.id == venue_id).first()
    if venue is None:
        raise HTTPException(status_code=404, detail="Venue not found")
    return venue
