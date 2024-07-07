# booking_platform/services/reservations/app/main.py

from fastapi import FastAPI
from .routers import reservation_router
from .models import Base
from .utils import engine

# Создание всех таблиц
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(reservation_router.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Booking Platform"}
