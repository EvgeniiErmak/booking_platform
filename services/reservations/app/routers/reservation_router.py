# booking_platform/services/reservations/app/routers/reservation_router.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from services.reservations.app import models, schemas, utils

router = APIRouter()


@router.post("/reservations/", response_model=schemas.ReservationCreate)
def create_reservation(reservation: schemas.ReservationCreate, db: Session = Depends(utils.get_db)):
    db_reservation = models.Reservation(**reservation.dict())
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation
