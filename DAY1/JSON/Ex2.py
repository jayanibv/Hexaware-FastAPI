#to write/create a json file

user= {"name": "Jayani", "age": 20, "city": "Hyderabad"}

import json
with open("user.json","w") as file:
    json.dump(user,file, indent=2)