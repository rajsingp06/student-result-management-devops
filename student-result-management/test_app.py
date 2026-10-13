import pytest
from app import app


@pytest.fixture()
def client():
    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client


def test_home_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json()["message"] == "Student Result Management System"


def test_result_101_has_expected_fields(client):
    response = client.get("/results/101")
    data = response.get_json()
    assert response.status_code == 200
    assert data["roll_number"] == 101
    assert data["total"] == 234
    assert data["percentage"] == 78.0
    assert data["status"] == "PASS"


def test_student_103_fails_if_any_subject_is_below_pass_mark(client):
    response = client.get("/results/103")
    assert response.status_code == 200
    assert response.get_json()["status"] == "FAIL"


def test_unknown_roll_number_returns_404(client):
    response = client.get("/results/999")
    assert response.status_code == 404
    assert response.get_json()["error"] == "Student not found"


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"
