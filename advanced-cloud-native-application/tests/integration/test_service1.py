import requests

def test_service1():
    response = requests.get("http://service1-service")
    assert response.status_code == 200
    assert response.text == "Hello from Service 1!"
