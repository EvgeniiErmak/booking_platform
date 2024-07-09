# booking_platform/Dockerfile

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY ./users /app/users
COPY ./reservations /app/reservations
COPY ./notifications /app/notifications
COPY ./venues /app/venues
COPY ./database.py /app/database.py
COPY ./init_db.py /app/init_db.py
COPY ./wait-for-it.sh /app/wait-for-it.sh

WORKDIR /app
