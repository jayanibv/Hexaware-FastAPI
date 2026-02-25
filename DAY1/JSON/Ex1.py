import json

student={
    "name": "Alice",
    "age": 20,
    "courses": ["Math", "Science"],
    "is_graduated": False
}

print (student)
#json.dumps() -> Python dict to JSON string
json_str= json.dumps(student)
print(json_str)
print(type(json_str))
print(json.dumps(student,indent=2))

#json.loads() -> JSON string to Python dict
python_dict= json.loads(json_str)
print(python_dict)
print(type(python_dict))
