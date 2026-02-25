To create a virtual environement
python -m venv venv
.\venv\Scripts\Activate.ps1  (or)
venv\Scripts\activate
pip intall dotenv
pip list

pip install pydantic fastapi uvicorn

uv is excellent and fast now
uv venv
.\.venv\Scripts\Activate.ps1
uv add python-dotenv

running the app
uvicorn main:app --reload
or
uvicorn app.main:app --reload
or
uvicorn app.main:app --reload --port 8001

Client
  |
  V
Controller (API layer)
  |
  V
Service (Business logic layer)
  |
  V
Repository (Data layer)

depenedncy works in controller and not in repository

My notes:
1st start with schema (create a BaseModel)
2nd with services (create a class and initialize it with repository)
3rd with repository (create a class and initialize it with database)
4th dependency (import repository and service and create a dependency function and return the service)
5th controller (import dependency and create a controller function and return the service)
6th middleware
7th main (import controller and create a router and include the controller)

Create folder structure yourself
Start from schemas - define BaseModel, uses Pydantic
Then repository - define methods like create and get
Then service - logic - connect repository
Then controller - connect service, endpoints (GET, POST)
Then dependency- connect service and repository
Then main - connect controller and router, create app, register middleware


TO run migration and test case

rm alembic.ini (remove alembic.ini)
rm alembic (remove alembic folder)
Goto alembic.ini and change the url
sqlalchemy.url=sqlite:///./test.db

How to check
alembic upgrade head

run the testcases
pytest -V

Purpose of alembic
1. To create a migration file
2. To upgrade the database
3. To downgrade the database
4. Modify schema