from microservices.service2.app import hello_service2

def test_hello_service2():
    assert hello_service2() == "Hello from Service 2!"
