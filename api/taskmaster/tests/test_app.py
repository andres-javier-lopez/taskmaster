from taskmaster import __version__


def test_version(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert __version__ in response.text


def test_ping(test_client):
    response = test_client.get("/ping")
    assert response.status_code == 200
    assert response.text == "pong"
