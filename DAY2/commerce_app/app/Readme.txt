create_engine
connect to the database

settings
configuration

sessionmaker
factory for creating sessions

declarative_base
Used to define ORM models (tables)

dependency injection
FastAPI dependency injection pattern it has to follow

engine
Used to connect to the database
core connection interface
talks to postgreSQL

Session
temporary DB conversation
executes queries
handles transactions

Base Class
all models inherit from this
helps SQL Alchemy
maps class to table

API request comes
1. create DB session
2. pass it to API
3. Execute API logic
4. Close DB session

yield
instead of return

Starlette
lightweight ASGI framework
used by FastAPI
for routing, middleware, REquest/REsponse, exception handling
API extends Starlette with Data validation(Pydantic), Depenedency Injection, Auto-docs(Swagger/OpenAPI), Type-hint support