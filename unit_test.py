import pytest
from Flask_App import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_hello(client):
    """
    This test ensures the web app returns a 200 OK status 
    and the correct text. Jenkins will run this automatically.
    """
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, DevSecOps" in response.data