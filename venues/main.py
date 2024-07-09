# booking_platform/venues/main.py

from fastapi import FastAPI
from database import engine
from venues import models
from venues.routers import venue

app = FastAPI()

# Проверка подключения к базе данных
try:
    with engine.connect() as conn:
        print("Successfully connected to the database.")
except Exception as e:
    print(f"Error connecting to the database: {e}")

models.Base.metadata.create_all(bind=engine)

app.include_router(venue.router, prefix="/venues", tags=["venues"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the Venue Management Service"}
