from fastapi import FastAPI, Request
import time
from app.controllers import event_controller, participant_controller
from app.middleware.cors_middleware import add_cors_middleware

app = FastAPI(title="Event Management API")

# Add CORS middleware
add_cors_middleware(app)

# Logging Middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    print(f"Method: {request.method} Path: {request.url.path} Status: {response.status_code} Time: {process_time:.4f}s")
    return response

# Include routers
app.include_router(event_controller.router)
app.include_router(participant_controller.router)