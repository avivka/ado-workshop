from service1.app import app
import pytest

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_service1_endpoint(client):
    response = client.get('/api/data')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["message"] == "Hello from Service 1!"