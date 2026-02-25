My notes:
1st start with schema (create a BaseModel)
2nd with services (create a class and initialize it with repository)
3rd with repository (create a class and initialize it with database)
4th dependency (import repository and service and create a dependency function and return the service)
5th controller (import dependency and create a controller function and return the service)
6th middleware
7th main (import controller and create a router and include the controller)
