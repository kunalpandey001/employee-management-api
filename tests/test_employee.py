from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_create_employee():
    employee_data = {
        "name": "Test Employee",
        "email": "test.employee3@example.com",
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
    assert data["email"] == "test.employee3@example.com"
    assert data["department"] == "Engineering"
    assert data["designation"] == "Python Developer"
    assert "id" in data


def test_get_employee_by_id():
    employee_data = {
        "name": "Get Test Employee",
        "email": "get.test.employee2@example.com",
        "department": "Engineering",
        "designation": "Python Developer"
    }

    create_response = client.post(
        "/employees/",
        json=employee_data
    )

    assert create_response.status_code == 201

    employee_id = create_response.json()["id"]

    response = client.get(
        f"/employees/{employee_id}"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == employee_id
    assert data["name"] == "Get Test Employee"
    assert data["email"] == "get.test.employee2@example.com"