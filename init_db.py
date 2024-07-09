# booking_platform/init_db.py

from sqlalchemy import create_engine
from database import Base, engine
from users import models as user_models
from venues import models as venue_models


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()
