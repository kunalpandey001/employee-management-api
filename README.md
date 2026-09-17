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
- Filtering and sorting
- Pagination metadata
- Input validation
- Duplicate email handling
- PostgreSQL
- SQLAlchemy
- Alembic migrations
- Pytest
- Docker
- GitHub Actions
- Swagger API documentation

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
| Docker | Containerization |
| GitHub Actions | Continuous integration |

## Architecture

```text
Client
   |
   v
FastAPI
   |
   v
Routes
   |
   v
Services
   |
   v
SQLAlchemy
   |
   v
PostgreSQL