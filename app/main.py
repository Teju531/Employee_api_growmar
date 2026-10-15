from fastapi import FastAPI
from app.routes.employees import router as employees_router
from app.routes.departments import router as departments_router

app = FastAPI(title="Employee API")

app.include_router(employees_router)
app.include_router(departments_router)

@app.get("/health")
def health_check():
    return {"status": "ok"}