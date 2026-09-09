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