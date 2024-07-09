# booking_platform/venues/main.py

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import engine, get_db
from venues import models, schemas, crud
from venues.routers import venue

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(venue.router, prefix="/venues", tags=["venues"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the Venue Management Service"}


@app.post("/venues/", response_model=schemas.Venue)
def create_venue(venue: schemas.VenueCreate, db: Session = Depends(get_db)):
    db_venue = crud.get_venue_by_name(db, name=venue.name)
    if db_venue:
        raise HTTPException(status_code=400, detail="Venue already exists")
    return crud.create_venue(db=db, venue=venue)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
