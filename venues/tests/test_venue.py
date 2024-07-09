# booking_platform/venues/tests/test_venue.py

from fastapi.testclient import TestClient
from venues.main import app

client = TestClient(app)


def test_create_venue():
    response = client.post("/venues/", json={"name": "Test Venue", "address": "123 Test St", "capacity": 100})
    assert response.status_code == 200
    assert response.json()["name"] == "Test Venue"


def test_read_venues():
    response = client.get("/venues/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_read_venue():
    response = client.get("/venues/1")
    assert response.status_code == 200 or response.status_code == 404


def test_update_venue():
    response = client.put("/venues/1", json={"name": "Updated Venue", "address": "123 Updated St", "capacity": 150, "is_active": True})
    assert response.status_code == 200 or response.status_code == 404


def test_delete_venue():
    response = client.delete("/venues/1")
    assert response.status_code == 200 or response.status_code == 404
