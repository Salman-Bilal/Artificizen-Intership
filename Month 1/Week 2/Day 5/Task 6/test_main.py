from fastapi.testclient import TestClient
from main import app, users

client = TestClient(app)


def setup_function():
    users.clear()


def test_create_user():
    response = client.post(
        "/users",
        json={
            "name": "Salman",
            "email": "salman@gmail.com"
        }
    )

    assert response.status_code == 201
    assert response.json()["email"] == "salman@gmail.com"


def test_duplicate_email():

    client.post(
        "/users",
        json={
            "name": "Salman",
            "email": "salman@gmail.com"
        }
    )

    response = client.post(
        "/users",
        json={
            "name": "Ali",
            "email": "salman@gmail.com"
        }
    )

    assert response.status_code == 409
    assert response.json()["detail"] == "Email already exists"


def test_protected_route_without_token():

    response = client.get("/profile")

    assert response.status_code == 401
    assert response.json()["detail"] == "Not authenticated"