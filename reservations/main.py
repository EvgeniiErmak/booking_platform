# booking_platform/reservations/main.py

from fastapi import FastAPI
from database import engine
from users import models as user_models
from venues import models as venue_models
from reservations import models
from reservations.routers import reservation

# Сначала создаем таблицы пользователей и заведений
user_models.Base.metadata.create_all(bind=engine)
venue_models.Base.metadata.create_all(bind=engine)
# Затем создаем таблицы броней
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(reservation.router, prefix="/reservations", tags=["reservations"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the Reservations Management Service"}
