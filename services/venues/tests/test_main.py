# booking_platform/services/venues/tests/test_main.py

import sys
import os

# Добавляем путь к корневому каталогу проекта
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from fastapi.testclient import TestClient
from services.venues.app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Venue Management Service"}


def test_create_venue():
    response = client.post(
        "/venues/",
        json={"name": "Central Park", "location": "New York"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Central Park"
    assert response.json()["location"] == "New York"


def test_read_venue():
    response = client.post(
        "/venues/",
        json={"name": "Central Park", "location": "New York"}
    )
    venue_id = response.json()["id"]
    response = client.get(f"/venues/{venue_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Central Park"
    assert response.json()["location"] == "New York"
