from fastapi import FastAPI
from app.database.session import engine
from app.database.base import Base

# Import models explicitly (important)
from app.models.user import User
from app.models.department import Department
from app.models.asset import Asset
from app.models.asset_assignment import AssetAssignment
from app.models.asset_request import AssetRequest

# Routers
from app.routers.auth_router import router as auth_router
from app.routers.superadmin_router import router as superadmin_router
from app.routers.itadmin_router import router as itadmin_router
from app.routers.manager_router import router as manager_router
from app.routers.employee_router import router as employee_router

# Middleware
from app.middleware.logging import LoggingMiddleware
from app.middleware.exception_handler import (
    global_exception_handler,
    http_exception_handler
)
from fastapi.exceptions import HTTPException as FastAPIHTTPException


app = FastAPI(title="Enterprise Asset Management System")


# Create tables
Base.metadata.create_all(bind=engine)


# Middleware
app.add_middleware(LoggingMiddleware)

app.add_exception_handler(Exception, global_exception_handler)
app.add_exception_handler(FastAPIHTTPException, http_exception_handler)


# Routers
app.include_router(auth_router)
app.include_router(superadmin_router)
app.include_router(itadmin_router)
app.include_router(manager_router)
app.include_router(employee_router)


@app.get("/")
def root():
    return {"message": "EAMS Running"}