from fastapi.testclient import TestClient

from app.main import app
from app.routes import get_db
from tests.conftest import TestingSessionLocal


def override_get_db():
    db = TestingSessionLocal()

    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_create_employee():
    employee_data = {
        "name": "Test Employee",
        "email": "test.create.unique@example.com",
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
    assert data["email"] == "test.create.unique@example.com"
    assert data["department"] == "Engineering"
    assert data["designation"] == "Python Developer"
    assert "id" in data


def test_get_employee_by_id():
    employee_data = {
        "name": "Get Test Employee",
        "email": "get.test.unique@example.com",
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
    assert data["email"] == "get.test.unique@example.com"


def test_update_employee():
    employee_data = {
        "name": "Update Test Employee",
        "email": "update.test.unique@example.com",
        "department": "Engineering",
        "designation": "Python Developer"
    }

    create_response = client.post(
        "/employees/",
        json=employee_data
    )

    assert create_response.status_code == 201

    employee_id = create_response.json()["id"]

    updated_data = {
        "name": "Updated Employee",
        "email": "updated.test.unique@example.com",
        "department": "Software Engineering",
        "designation": "Senior Python Developer"
    }

    response = client.put(
        f"/employees/{employee_id}",
        json=updated_data
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == employee_id
    assert data["name"] == "Updated Employee"
    assert data["email"] == "updated.test.unique@example.com"
    assert data["department"] == "Software Engineering"
    assert data["designation"] == "Senior Python Developer"


def test_delete_employee():
    employee_data = {
        "name": "Delete Test Employee",
        "email": "delete.test.unique@example.com",
        "department": "Engineering",
        "designation": "Python Developer"
    }

    create_response = client.post(
        "/employees/",
        json=employee_data
    )

    assert create_response.status_code == 201

    employee_id = create_response.json()["id"]

    response = client.delete(
        f"/employees/{employee_id}"
    )

    assert response.status_code == 200

    assert response.json() == {
        "message": "Employee deleted successfully"
    }

    get_response = client.get(
        f"/employees/{employee_id}"
    )

    assert get_response.status_code == 404