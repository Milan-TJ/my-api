from fastapi.testclient import TestClient
from app.main import app, add

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_add():
    response = client.post("/add", params={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 5}

def test_sub():
    response = client.post("/sub", params={"a": 5, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 2}