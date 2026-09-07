\# Employee Management API



A RESTful Employee Management API built with Python and FastAPI, using PostgreSQL and SQLAlchemy.



\## Features



\- Create employees

\- Get all employees

\- Get employee by ID

\- Update employees

\- Delete employees

\- Search employees

\- Pagination

\- Filtering by department and designation

\- Sorting by employee fields

\- Input validation with Pydantic

\- Proper HTTP status codes

\- Duplicate email handling

\- PostgreSQL database

\- SQLAlchemy ORM

\- Alembic database migrations

\- Interactive Swagger API documentation



\## Tech Stack



\- Python

\- FastAPI

\- PostgreSQL

\- SQLAlchemy

\- Pydantic

\- Alembic

\- Uvicorn

\- Docker

\- Git \& GitHub



\## Project Structure



```text

employee-management-api/

│

├── alembic/

│   ├── versions/

│   ├── env.py

│   └── script.py.mako

│

├── app/

│   ├── database.py

│   ├── main.py

│   ├── models.py

│   ├── routes.py

│   ├── schemas.py

│   └── services.py

│

├── .env

├── .gitignore

├── alembic.ini

└── README.md

