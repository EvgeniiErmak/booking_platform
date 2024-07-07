# booking_platform/services/users/tests/test_main.py

from fastapi.testclient import TestClient
from ..app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the User Management Service"}


def test_create_user():
    response = client.post(
        "/users/",
        json={"name": "John Doe", "email": "john@example.com"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "john@example.com"


def test_read_user():
    response = client.post(
        "/users/",
        json={"name": "John Doe", "email": "john@example.com"}
    )
    user_id = response.json()["id"]
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "john@example.com"
