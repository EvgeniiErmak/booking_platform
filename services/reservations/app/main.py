# booking_platform/services/reservations/app/main.py

from fastapi import FastAPI
import sys
import os

sys.path.append('/app')

from services.reservations.app.routers import reservation_router
from services.reservations.app import models, schemas, utils

# Создание всех таблиц
models.Base.metadata.create_all(bind=utils.engine)

app = FastAPI()

app.include_router(reservation_router.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Booking Platform"}
