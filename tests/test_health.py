from fastapi.testclient import TestClient

from services.routing_server.app.main import app as routing_app
from services.admin_server.app.main import app as admin_app


def test_routing_health():
    c = TestClient(routing_app)
    r = c.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_admin_health():
    c = TestClient(admin_app)
    r = c.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"
