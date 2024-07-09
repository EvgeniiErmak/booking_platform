# booking_platform/services/venues/app/main.py

from fastapi import FastAPI
import sys
import os

sys.path.append('/app')

from services.venues.app.routers import venue_router
from services.venues.app import models, schemas, utils

# Создание всех таблиц
models.Base.metadata.create_all(bind=utils.engine)

app = FastAPI()

app.include_router(venue_router.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Venue Management Service"}
