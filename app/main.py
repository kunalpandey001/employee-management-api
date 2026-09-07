from fastapi import FastAPI
from app.routes import router as employee_router

app = FastAPI(
    title="Employee Management API",
    description="A REST API for managing employees",
    version="1.0.0"
)

app.include_router(employee_router)


@app.get("/", tags=["System"])
def root():
    return {
        "message": "Employee Management API is running"
    }


@app.get("/health", tags=["System"])
def health_check():
    return {
        "status": "healthy"
    }