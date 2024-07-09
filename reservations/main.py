# booking_platform/reservations/main.py

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import engine, get_db
from users import models as user_models
from venues import models as venue_models
from reservations import models, schemas, crud
from reservations.routers import reservation

# Создаем таблицы для всех моделей
user_models.Base.metadata.create_all(bind=engine)
venue_models.Base.metadata.create_all(bind=engine)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(reservation.router, prefix="/reservations", tags=["reservations"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the Reservations Management Service"}


@app.post("/reservations/", response_model=schemas.Reservation)
def create_reservation(reservation: schemas.ReservationCreate, db: Session = Depends(get_db)):
    db_user = db.query(user_models.User).filter(user_models.User.id == reservation.user_id).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="User not found")

    db_venue = db.query(venue_models.Venue).filter(venue_models.Venue.id == reservation.venue_id).first()
    if not db_venue:
        raise HTTPException(status_code=400, detail="Venue not found")

    return crud.create_reservation(db=db, reservation=reservation)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
