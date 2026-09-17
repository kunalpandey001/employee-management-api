# Employee Management API

A production-style RESTful Employee Management API built with Python, FastAPI, PostgreSQL, and SQLAlchemy.

The project demonstrates REST API design, validation, database migrations, automated testing, Docker containerization, and continuous integration with GitHub Actions.

## Features

- Create employees
- Get employees with pagination
- Get employee by ID
- Update employees
- Delete employees
- Search employees
- Filter by department and designation
- Sort by employee fields
- Pagination metadata
- Input validation with Pydantic
- Duplicate email handling
- Proper HTTP status codes
- PostgreSQL database
- SQLAlchemy ORM
- Alembic database migrations
- Docker and Docker Compose
- Automated tests with Pytest
- GitHub Actions CI
- Interactive Swagger API documentation

## Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.12 | Programming language |
| FastAPI | REST API framework |
| PostgreSQL 16 | Database |
| SQLAlchemy | ORM |
| Pydantic | Data validation |
| Alembic | Database migrations |
| Pytest | Testing |
| Uvicorn | ASGI server |
| Docker | Containerization |
| Docker Compose | Multi-container development |
| GitHub Actions | Continuous integration |
| Git & GitHub | Version control |

## Architecture

```text
Client / Swagger / Postman
            |
            v
        FastAPI
            |
            v
       Route Layer
            |
            v
      Service Layer
            |
            v
      SQLAlchemy ORM
            |
            v
       PostgreSQL
```

## Project Structure

```text
employee-management-api/
|
+-- .github/
|   +-- workflows/
|       +-- ci.yml
|
+-- alembic/
|   +-- versions/
|   +-- env.py
|   +-- script.py.mako
|
+-- app/
|   +-- database.py
|   +-- main.py
|   +-- models.py
|   +-- routes.py
|   +-- schemas.py
|   +-- services.py
|
+-- tests/
|   +-- __init__.py
|   +-- conftest.py
|   +-- test_employee.py
|   +-- test_health.py
|
+-- .dockerignore
+-- .env.example
+-- .gitignore
+-- alembic.ini
+-- docker-compose.yml
+-- Dockerfile
+-- README.md
+-- requirements.txt
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/employees/` | Create an employee |
| GET | `/employees/` | Get employees |
| GET | `/employees/{employee_id}` | Get employee by ID |
| PUT | `/employees/{employee_id}` | Update an employee |
| DELETE | `/employees/{employee_id}` | Delete an employee |
| GET | `/employees/search` | Search employees |

## Pagination

```text
GET /employees/?skip=0&limit=10
```

Example response:

```json
{
  "items": [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john@example.com",
      "department": "Engineering",
      "designation": "Python Developer"
    }
  ],
  "total": 1,
  "skip": 0,
  "limit": 10
}
```

## Filtering

```text
GET /employees/?department=Engineering
GET /employees/?designation=Developer
```

## Sorting

```text
GET /employees/?sort_by=name&order=asc
```

Supported fields:

```text
id
name
email
department
designation
```

Supported orders:

```text
asc
desc
```

## Search

```text
GET /employees/search?name=Rahul
GET /employees/search?department=Engineering
GET /employees/search?designation=Developer
```

Multiple filters:

```text
GET /employees/search?department=Engineering&designation=Backend
```

## Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/kunalpandey001/employee-management-api.git
cd employee-management-api
```

### 2. Create a virtual environment

```powershell
python -m venv venv
```

### 3. Activate the virtual environment

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file:

```env
DATABASE_URL=postgresql://employee_user:employee_pass@localhost:5432/employee_db
```

### 6. Run database migrations

```powershell
alembic upgrade head
```

### 7. Start the API

```powershell
uvicorn app.main:app --reload
```

API:

```text
http://localhost:8000
```

## API Documentation

Swagger UI:

```text
http://localhost:8000/docs
```

ReDoc:

```text
http://localhost:8000/redoc
```

Health check:

```text
http://localhost:8000/health
```

## Running with Docker

Start the application and PostgreSQL:

```powershell
docker compose up -d
```

Check containers:

```powershell
docker compose ps
```

Run migrations:

```powershell
docker compose exec api alembic upgrade head
```

Stop containers:

```powershell
docker compose down
```

## Running Tests

```powershell
pytest
```

The test suite covers:

- Employee creation
- Employee retrieval
- Employee updates
- Employee deletion
- Employee search
- Pagination
- Pagination validation
- Sorting
- Invalid sorting
- Duplicate email handling
- Missing employee handling
- Health check

## Database Migrations

Create a new migration:

```powershell
alembic revision --autogenerate -m "describe your change"
```

Apply migrations:

```powershell
alembic upgrade head
```

Rollback the latest migration:

```powershell
alembic downgrade -1
```

## Environment Variables

The application uses the `DATABASE_URL` environment variable.

Example:

```env
DATABASE_URL=postgresql://employee_user:employee_pass@localhost:5432/employee_db
```

The actual `.env` file is excluded from Git.

A safe template is provided in:

```text
.env.example
```

## Continuous Integration

GitHub Actions runs automatically on pushes to the `master` branch and on pull requests.

The CI pipeline:

1. Starts PostgreSQL
2. Sets up Python 3.12
3. Installs dependencies
4. Runs Alembic migrations
5. Runs Pytest

## Error Handling

Common HTTP responses:

```text
200 OK
201 Created
400 Bad Request
404 Not Found
409 Conflict
422 Unprocessable Entity
```

Duplicate email example:

```json
{
  "detail": "Email already registered"
}
```

## Development Practices

- REST API development
- Layered architecture
- SQLAlchemy ORM
- Pydantic validation
- Dependency injection
- Database migrations
- Automated testing
- Test fixtures
- Environment configuration
- Docker containerization
- Continuous integration
- Git version control

## Author

**Kunal Pandey**

GitHub: https://github.com/kunalpandey001