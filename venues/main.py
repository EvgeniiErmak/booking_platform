# booking_platform/venues/main.py

from fastapi import FastAPI
from database import engine
from venues import models
from venues.routers import venue

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(venue.router, prefix="/venues", tags=["venues"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the Venue Management Service"}
