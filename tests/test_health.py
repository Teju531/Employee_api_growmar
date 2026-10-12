from fastapi.testclient import TestClient
from app.main import app

#cretaing an new test client for api
client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200 #if succeded
    assert response.json() == {"status": "ok"}