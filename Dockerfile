# booking_platform/Dockerfile

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt
RUN apt-get update && apt-get install -y netcat-openbsd

COPY ./users /app/users
COPY ./database.py /app/database.py
COPY ./init_db.py /app/init_db.py
COPY ./wait-for-it.sh /app/wait-for-it.sh

WORKDIR /app/users

CMD ["sh", "-c", "/app/wait-for-it.sh db -- python /app/init_db.py && uvicorn main:app --host 0.0.0.0 --port 8000"]
