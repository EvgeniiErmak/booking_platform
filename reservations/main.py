# booking_platform/reservations/main.py

from fastapi import FastAPI
from database import engine
from reservations import models
from reservations.routers import reservation

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(reservation.router, prefix="/reservations", tags=["reservations"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the Reservation Management Service"}
