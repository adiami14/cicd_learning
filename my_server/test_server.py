import pytest
from server_side import app


@pytest.fixture
def client():
    """Create a test client for the Flask app"""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_add_user_success(client):
    """Test adding a new user"""
    response = client.post("/add_user", json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 201
    assert "New user 'John Doe' added successfully" in response.json["message"]

def test_add_user_invalid_data(client):
    """Test adding a user with missing fields"""
    response = client.post("/add_user", json={})
    assert response.status_code == 400
    assert "Invalid data" in response.json["error"]

def test_get_users(client):
    """Test retrieving user list"""
    # Add a user first
    client.post("/add_user", json={"name": "Alice", "email": "alice@example.com"})

    response = client.get("/users")
    assert response.status_code == 200
    users = response.json["users"]
    assert any(user["name"] == "Alice" for user in users)
