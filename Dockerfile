# booking_platform/Dockerfile

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY ./users /app/users
COPY ./database.py /app/database.py

WORKDIR /app/users
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
