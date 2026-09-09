import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_users_list():
    response = requests.get(f"{BASE_URL}/users")
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_single_user_details():
    response = requests.get(f"{BASE_URL}/users/1")
    data = response.json()

    assert response.status_code == 200
    assert data["id"] == 1
    assert "email" in data
    assert "company" in data