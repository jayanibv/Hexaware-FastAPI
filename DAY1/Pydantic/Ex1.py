from pydantic import BaseModel, ValidationError, StrictInt

class User(BaseModel):
    name: str
    age: StrictInt
    email: str

try:
    user = User (name="Jay", age=22, email="jay@mail.com")
    print(user.dict())
except ValidationError as e:
    print(e)