# booking_platform/services/reservations/tests/test_main.py

from fastapi.testclient import TestClient
from ..app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Booking Platform"}


def test_create_reservation():
    response = client.post(
        "/reservations/",
        json={"user_id": 1, "venue_id": 1, "date": "2023-07-07T12:00:00"}
    )
    assert response.status_code == 200
    assert response.json()["user_id"] == 1
    assert response.json()["venue_id"] == 1
