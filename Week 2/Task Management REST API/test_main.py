from fastapi.testclient import TestClient
import pytest
from database import engine, Base
from main import app

# Create a clean database state for our test sessions
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

client = TestClient(app)

# Helper token variable to share state between test runs
auth_headers = {}

# 1. Test Register
def test_register():
    response = client.post("/auth/register", json={
        "email": "tester@example.com",
        "password": "strongpassword"
    })
    assert response.status_code == 201
    assert response.json()["email"] == "tester@example.com"

# 2. Test Login
def test_login():
    global auth_headers
    response = client.post("/auth/login", data={
        "username": "tester@example.com",
        "password": "strongpassword"
    })
    assert response.status_code == 200
    token = response.json()["access_token"]
    auth_headers = {"Authorization": f"Bearer {token}"}

# 3. Test Create Task
def test_create_task():
    response = client.post("/tasks/", json={
        "title": "Finish Capstone Project",
        "description": "Implement CRUD and testing",
        "status": "pending",
        "due_date": "2026-07-15"
    }, headers=auth_headers)
    assert response.status_code == 201
    assert response.json()["title"] == "Finish Capstone Project"

# 4. Test Fetch Tasks
def test_fetch_tasks():
    response = client.get("/tasks/", headers=auth_headers)
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["title"] == "Finish Capstone Project"

# 5. Test Unauthorized Access
def test_unauthorized_access():
    response = client.get("/tasks/") # Missing auth headers!
    assert response.status_code == 401
    assert response.json()["error"] is True