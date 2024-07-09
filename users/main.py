# booking_platform/users/main.py

from fastapi import FastAPI
from users.routers import user

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "User management microservice is running"}


app.include_router(user.router, prefix="/users", tags=["users"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
