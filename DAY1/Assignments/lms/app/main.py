from fastapi import FastAPI
from app.controllers import student_controller, course_controller, enrollment_controller
from app.middleware.cors import add_cors_middleware

app = FastAPI(title="LMS API")

add_cors_middleware(app)

print("This is my LMS project")

app.include_router(student_controller.router)
app.include_router(course_controller.router)
app.include_router(enrollment_controller.router)