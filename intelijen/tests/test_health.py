from fastapi.testclient import TestClient

from backend.main import app


client = TestClient(app)


def test_health_endpoint_returns_expected_payload() -> None:
    response = client.get("/api/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "application": "INTELIJEN",
        "version": "0.1.0",
    }
