"""Basic API contract checks against isolated, temporary SQLite databases."""

from fastapi.testclient import TestClient

from app.main import create_app


def make_client(tmp_path):
    return TestClient(create_app(str(tmp_path / "tickets.db")))


def test_health(tmp_path):
    result = make_client(tmp_path).get("/health")
    assert result.status_code == 200
    assert result.json() == {"status": "ok"}


def test_create_read_and_list_ticket(tmp_path):
    api = make_client(tmp_path)
    result = api.post(
        "/tickets",
        json={
            "title": "Demo incident",
            "description": "Fictieve printer is offline",
            "category": "incident",
        },
    )
    assert result.status_code == 201
    ticket = result.json()
    assert ticket["status"] == "open"
    assert ticket["category"] == "incident"
    assert api.get(f"/tickets/{ticket['id']}").json()["title"] == "Demo incident"
    assert len(api.get("/tickets").json()) == 1


def test_invalid_input_returns_422(tmp_path):
    result = make_client(tmp_path).post(
        "/tickets", json={"title": "x", "description": "a"}
    )
    assert result.status_code == 422


def test_missing_ticket_returns_404(tmp_path):
    assert make_client(tmp_path).get("/tickets/999").status_code == 404


def test_sql_metacharacters_are_not_executed(tmp_path):
    api = make_client(tmp_path)
    result = api.post(
        "/tickets",
        json={
            "title": "Input test",
            "description": "x'); DROP TABLE tickets; --",
        },
    )
    assert result.status_code == 201
    assert api.get("/tickets").status_code == 200
