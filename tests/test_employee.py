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


def test_create_employee(employee_data):
    response = client.post(
        "/employees/",
        json=employee_data
    )

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == employee_data["name"]
    assert data["email"] == employee_data["email"]
    assert data["department"] == employee_data["department"]
    assert data["designation"] == employee_data["designation"]
    assert "id" in data


def test_get_employee_by_id(employee_data):
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
    assert data["name"] == employee_data["name"]
    assert data["email"] == employee_data["email"]


def test_update_employee(employee_data):
   
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


def test_delete_employee(employee_data):
   
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


def test_search_employee_by_name(search_employee_data):

    create_response = client.post(
        "/employees/",
        json=search_employee_data
    )

    assert create_response.status_code == 201

    response = client.get(
        "/employees/search?name=Rahul"
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 1
    assert data[0]["name"] == "Rahul Sharma"


def test_search_employee_by_department(department_search_employee_data):
    

    create_response = client.post(
        "/employees/",
        json=department_search_employee_data
    )

    assert create_response.status_code == 201

    response = client.get(
        "/employees/search?department=Data"
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 1
    assert data[0]["department"] == "Data Science"

def test_employee_pagination(pagination_employees):
    for employee in pagination_employees:
        response = client.post(
            "/employees/",
            json=employee
        )

        assert response.status_code == 201

    response = client.get(
        "/employees/?skip=1&limit=1"
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data["items"]) == 1
    assert data["items"][0]["name"] == pagination_employees[1]["name"]

    assert data["total"] == 3
    assert data["skip"] == 1
    assert data["limit"] == 1

def test_employee_pagination_limit_validation():
    response = client.get(
        "/employees/?limit=101"
    )

    assert response.status_code == 422

def test_employee_sorting(pagination_employees):
    for employee in pagination_employees:
        response = client.post(
            "/employees/",
            json=employee
        )

        assert response.status_code == 201

    response = client.get(
        "/employees/?sort_by=name&order=asc"
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data["items"]) == 3
    assert data["items"][0]["name"] == pagination_employees[0]["name"]
    assert data["items"][1]["name"] == pagination_employees[2]["name"]
    assert data["items"][2]["name"] == pagination_employees[1]["name"]

    assert data["total"] == 3
    assert data["skip"] == 0
    assert data["limit"] == 10

def test_employee_invalid_sort_field():
    response = client.get(
        "/employees/?sort_by=invalid"
    )

    assert response.status_code == 400
    assert response.json() == {
        "detail": "Invalid sort_by field"
    }

def test_create_duplicate_email(employee_data):
    first_response = client.post(
        "/employees/",
        json=employee_data
    )

    assert first_response.status_code == 201

    duplicate_response = client.post(
        "/employees/",
        json=employee_data
    )

    assert duplicate_response.status_code == 409
    assert duplicate_response.json() == {
        "detail": "Email already registered"
    }


def test_get_nonexistent_employee():
    response = client.get(
        "/employees/999999"
    )

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Employee not found"
    }