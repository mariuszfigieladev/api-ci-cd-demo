import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_posts_status_code():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200

def test_get_single_post_schema():
    response = requests.get(f"{BASE_URL}/posts/1")
    data = response.json()
    
    assert response.status_code == 200
    assert data["id"] == 1
    assert "title" in data
    assert "body" in data