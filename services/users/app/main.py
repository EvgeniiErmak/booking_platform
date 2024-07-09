# booking_platform/services/users/app/main.py

from fastapi import FastAPI
import sys
import os

sys.path.append('/app')

from services.users.app.routers import user_router
from services.users.app import models, schemas, utils

# Создание всех таблиц
models.Base.metadata.create_all(bind=utils.engine)

app = FastAPI()

app.include_router(user_router.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the User Management Service"}
