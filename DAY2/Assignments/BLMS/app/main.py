from fastapi import FastAPI

from app.core.database import Base, engine

from app.middleware.cors import add_cors
from app.middleware.logging_middleware import LoggingMiddleware

from app.controllers import (
    user_controller,
    product_controller,
    application_controller,
    repayment_controller,
)


app = FastAPI(title="Banking Loan Management System")


# create tables
Base.metadata.create_all(bind=engine)


# middleware
add_cors(app)
app.add_middleware(LoggingMiddleware)


# routers
app.include_router(user_controller.router)
app.include_router(product_controller.router)
app.include_router(application_controller.router)
app.include_router(repayment_controller.router)