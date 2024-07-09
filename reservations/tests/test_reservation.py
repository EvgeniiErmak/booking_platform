# booking_platform/reservations/tests/test_reservation.py

from fastapi.testclient import TestClient
from reservations.main import app

client = TestClient(app)


def test_create_reservation():
    response = client.post(
        "/reservations/",
        json={"user_id": 1, "venue_id": 1, "start_time": "2023-07-09T14:00:00", "end_time": "2023-07-09T16:00:00", "status": "confirmed"},
    )
    assert response.status_code == 200
    assert response.json()["user_id"] == 1


def test_read_reservation():
    response = client.get("/reservations/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_delete_reservation():
    response = client.delete("/reservations/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
