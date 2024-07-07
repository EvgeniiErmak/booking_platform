# booking_platform/services/venues/app/main.py

from fastapi import FastAPI
from .routers import venue_router
from .models import Base
from .utils import engine

# Создание всех таблиц
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(venue_router.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Venue Management Service"}
