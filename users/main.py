# booking_platform/users/main.py

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from users import models, schemas, crud
from database import engine, get_db
from users.routers import user

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router, prefix="/users", tags=["users"])


@app.get("/")
def read_root():
    return {"message": "User management microservice is running"}


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
