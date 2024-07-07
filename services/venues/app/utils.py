# booking_platform/services/venues/app/utils.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import urllib.parse

# Закодированные учетные данные
username = urllib.parse.quote_plus("postgres")
password = urllib.parse.quote_plus("12345")
host = "localhost"
dbname = "booking_db"

SQLALCHEMY_DATABASE_URL = f"postgresql://{username}:{password}@{host}/{dbname}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"client_encoding": "utf8"})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
