from fastapi import FastAPI
from app.database.session import engine
from app.database.base import Base
from app.routers import employee_router
from app.routers import auth_router
from app.routers import admin_router
from app.routers import manager_router
app = FastAPI(title="Enterprise Leave Management System")

Base.metadata.create_all(bind=engine)

app.include_router(employee_router.router)
app.include_router(auth_router.router)
app.include_router(admin_router.router)
app.include_router(manager_router.router)