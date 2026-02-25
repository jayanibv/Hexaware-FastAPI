# app/main.py
 
from fastapi import FastAPI
from app.routes import student_routes
 
app = FastAPI()
 
# Root Endpoint
@app.get("/")
def LandingPage():
    return {"message": "Student Registration API is running"}
 
# Include Student Routes
app.include_router(student_routes.router)