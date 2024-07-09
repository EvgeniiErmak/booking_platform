# booking_platform/init_db.py

from database import Base, engine
from users import models as user_models
from venues import models as venue_models
from reservations import models


def init_db():
    user_models.Base.metadata.create_all(bind=engine)
    venue_models.Base.metadata.create_all(bind=engine)
    models.Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()
