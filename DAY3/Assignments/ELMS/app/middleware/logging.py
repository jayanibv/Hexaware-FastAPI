import time
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request


class LoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):
        start_time = time.time()

        response = await call_next(request)

        duration = round(time.time() - start_time, 4)

        print(f"{request.method} {request.url.path} completed in {duration}s")

        return response