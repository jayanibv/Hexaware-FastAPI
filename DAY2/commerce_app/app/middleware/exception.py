from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
import traceback

class GlobalExceptionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except Exception as e:
            #logging exception details (instead of printing)
            print(f"Exception occured: {str(e)}")
            traceback.print_exc()

            #return user friendly error message
            return JSONResponse(
                status_code=500,
                content={"detail": "An unexpected error occured"}
            )