import pytest
import requests
from unittest.mock import patch
import client

@pytest.fixture
def mock_requests_post():
    """Mock requests.post for add_user"""
    with patch("requests.post") as mock_post:
        yield mock_post

@pytest.fixture
def mock_requests_get():
    """Mock requests.get for get_users"""
    with patch("requests.get") as mock_get:
        yield mock_get

def test_add_user_success(mock_requests_post):
    """Test adding a user in the client script"""
    mock_requests_post.return_value.status_code = 201
    mock_requests_post.return_value.json.return_value = {"message": "User added successfully"}

    response = requests.post("http://localhost:5000/add_user", json={"name": "John", "email": "john@example.com"})
    assert response.status_code == 201
    assert response.json()["message"] == "User added successfully"

def test_add_user_failure(mock_requests_post):
    """Test handling API failure in the client"""
    mock_requests_post.return_value.status_code = 400
    mock_requests_post.return_value.json.return_value = {"error": "Invalid data"}

    response = requests.post("http://localhost:5000/add_user", json={})
    assert response.status_code == 400
    assert response.json()["error"] == "Invalid data"

def test_get_users(mock_requests_get):
    """Test fetching users in the client script"""
    mock_requests_get.return_value.status_code = 200
    mock_requests_get.return_value.json.return_value = {"users": [{"name": "Alice", "email": "alice@example.com"}]}

    response = requests.get("http://localhost:5000/users")
    assert response.status_code == 200
    assert response.json()["users"][0]["name"] == "Alice"
