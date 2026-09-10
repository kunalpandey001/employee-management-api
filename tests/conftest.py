import pytest

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from app.routes import get_db
from app.main import app


TEST_DATABASE_URL = (
    "postgresql://employee_user:employee_pass@localhost:5432/employee_test_db"
)

test_engine = create_engine(TEST_DATABASE_URL)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=test_engine
)


@pytest.fixture
def db():
    session = TestingSessionLocal()

    try:
        yield session
    finally:
        session.rollback()
        session.close()


@pytest.fixture(autouse=True)
def clean_database(db):
    db.execute(
        text("TRUNCATE TABLE employees RESTART IDENTITY CASCADE")
    )
    db.commit()


@pytest.fixture
def employee_data():
    return {
        "name": "Test Employee",
        "email": "test.employee@example.com",
        "department": "Engineering",
        "designation": "Python Developer"
    }

@pytest.fixture
def search_employee_data():
    return {
        "name": "Rahul Sharma",
        "email": "rahul.search@example.com",
        "department": "Engineering",
        "designation": "Python Developer"
    }

@pytest.fixture
def department_search_employee_data():
    return {
        "name": "Priya Mehta",
        "email": "priya.search@example.com",
        "department": "Data Science",
        "designation": "Data Engineer"
    }

@pytest.fixture
def pagination_employees():
    return [
        {
            "name": "Employee One",
            "email": "pagination.one@example.com",
            "department": "Engineering",
            "designation": "Developer"
        },
        {
            "name": "Employee Two",
            "email": "pagination.two@example.com",
            "department": "Engineering",
            "designation": "Developer"
        },
        {
            "name": "Employee Three",
            "email": "pagination.three@example.com",
            "department": "Engineering",
            "designation": "Developer"
        }
    ]