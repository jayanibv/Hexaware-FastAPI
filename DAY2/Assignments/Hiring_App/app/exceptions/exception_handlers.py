from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions.custom_exceptions import (
    UserNotFoundException,
    JobNotFoundException,
    ApplicationNotFoundException,
    DuplicateUserException,
)


def register_exception_handlers(app):

    @app.exception_handler(UserNotFoundException)
    async def user_not_found_handler(
        request: Request,
        exc: UserNotFoundException
    ):

        return JSONResponse(
            status_code=404,
            content={
                "error": exc.message
            }
        )


    @app.exception_handler(JobNotFoundException)
    async def job_not_found_handler(
        request: Request,
        exc: JobNotFoundException
    ):

        return JSONResponse(
            status_code=404,
            content={
                "error": exc.message
            }
        )


    @app.exception_handler(ApplicationNotFoundException)
    async def application_not_found_handler(
        request: Request,
        exc: ApplicationNotFoundException
    ):

        return JSONResponse(
            status_code=404,
            content={
                "error": exc.message
            }
        )


    @app.exception_handler(DuplicateUserException)
    async def duplicate_user_handler(
        request: Request,
        exc: DuplicateUserException
    ):

        return JSONResponse(
            status_code=400,
            content={
                "error": exc.message
            }
        )