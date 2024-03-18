from microservices.service1.app import hello_service1

def test_hello_service1():
    assert hello_service1() == "Hello from Service 1!"
