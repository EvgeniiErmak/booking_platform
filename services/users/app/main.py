# booking_platform/services/users/app/main.py

from fastapi import FastAPI
from .routers import user_router
from .models import Base
from .utils import engine

# Создание всех таблиц
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the User Management Service"}
