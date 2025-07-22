from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_visit_increments():
    response = client.post("/visit")
    assert response.status_code == 200
    assert "visits" in response.json()

def test_stats():
    response = client.get("/stats")
    assert response.status_code == 200
    data = response.json()
    assert "uptime_seconds" in data
    assert "total_visits" in data
    assert "current_time" in data