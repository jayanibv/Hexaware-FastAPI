pip install fastapi uvicorn
pip list

to run the application
uvicorn main:app --reload

What is FastAPI?
uvicorns runs the app
generates swagger docs
used to create Rest APIs
very fastbuild APIs in python with less code and high performance
based on python type hints
automatic documentation
automatic validation

Why do we use uvicorn?
ASGI server
runs the app
fast and lightweight
server used to run FastAPI app

What is ASGI?
Asynchronous Server Gateway Interface
standard interface between async python web applications and web servers
allows async code to run in a web server
handles multiple requests at once
allows FastAPI to handle multiple users effectively using async

What does --reload do?
reloads the server when the code changes
auto restart the server
used for development
not used in production