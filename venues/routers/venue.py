# booking_platform/venues/routers/venue.py

from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from venues import models, schemas

router = APIRouter()


@router.post("/", response_model=schemas.Venue)
def create_venue(venue: schemas.VenueCreate, db: Session = Depends(get_db)):
    db_venue = models.Venue(**venue.dict())
    db.add(db_venue)
    db.commit()
    db.refresh(db_venue)
    return db_venue


@router.get("/", response_model=List[schemas.Venue])
def read_venues(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    venues = db.query(models.Venue).offset(skip).limit(limit).all()
    return venues


@router.get("/{venue_id}", response_model=schemas.Venue)
def read_venue(venue_id: int, db: Session = Depends(get_db)):
    venue = db.query(models.Venue).filter(models.Venue.id == venue_id).first()
    if venue is None:
        raise HTTPException(status_code=404, detail="Venue not found")
    return venue


@router.put("/{venue_id}", response_model=schemas.Venue)
def update_venue(venue_id: int, venue: schemas.VenueUpdate, db: Session = Depends(get_db)):
    db_venue = db.query(models.Venue).filter(models.Venue.id == venue_id).first()
    if db_venue is None:
        raise HTTPException(status_code=404, detail="Venue not found")
    for key, value in venue.dict().items():
        setattr(db_venue, key, value)
    db.commit()
    db.refresh(db_venue)
    return db_venue


@router.delete("/{venue_id}", response_model=schemas.Venue)
def delete_venue(venue_id: int, db: Session = Depends(get_db)):
    db_venue = db.query(models.Venue).filter(models.Venue.id == venue_id).first()
    if db_venue is None:
        raise HTTPException(status_code=404, detail="Venue not found")
    db.delete(db_venue)
    db.commit()
    return db_venue
