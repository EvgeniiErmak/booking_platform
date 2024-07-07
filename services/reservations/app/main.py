# booking_platform/services/reservations/app/main.py

from fastapi import FastAPI
from app.routers import reservation_router
from app.utils import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(reservation_router.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Booking Platform"}
