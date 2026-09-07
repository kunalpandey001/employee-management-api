from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_create_employee():
    employee_data = {
        "name": "Test Employee",
        "email": "test.employee@example.com",
        "department": "Engineering",
        "designation": "Python Developer"
    }

    response = client.post(
        "/employees/",
        json=employee_data
    )

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "Test Employee"
    assert data["email"] == "test.employee@example.com"
    assert data["department"] == "Engineering"
    assert data["designation"] == "Python Developer"
    assert "id" in data