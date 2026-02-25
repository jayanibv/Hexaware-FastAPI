from fastapi import FastAPI

from app.core.database import Base, engine
from app.middleware.cors import add_cors
from app.middleware.logging import LoggingMiddleware

from app.controllers import (
    user_controller,
    job_controller,
    application_controller
)

from app.exceptions.exception_handlers import register_exception_handlers


app = FastAPI(title="Hiring Application Backend")


# create tables
Base.metadata.create_all(bind=engine)


# middleware
add_cors(app)
app.add_middleware(LoggingMiddleware)


# exception handlers
register_exception_handlers(app)


# routers
app.include_router(user_controller.router)
app.include_router(job_controller.router)
app.include_router(application_controller.router)