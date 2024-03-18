import requests

def test_service2():
    response = requests.get("http://service2-service")
    assert response.status_code == 200
    assert response.text == "Hello from Service 2!"
