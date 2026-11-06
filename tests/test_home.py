import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app()
    return app.test_client()

def test_home_page_returns_200(client):
    response = client.get("/")

    assert response.status_code == 200

def test_home_page_shows_heading(client):
    response = client.get("/")

    assert b"<h1>Workout Tracker</h1>" in response.data

