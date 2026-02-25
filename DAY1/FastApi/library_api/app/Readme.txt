Architecture

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


tasks:
Get /book ->list all books
Use a service layer
Use a repository layerInject service using Depends()
No database - just in-memory list

My notes:
repository and schema is connected using dependency injection