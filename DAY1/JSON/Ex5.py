import json
def parse_json(raw):
    try:
        return json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"InvalidJSON: {e}")
        return None

data = parse_json('{"name": "John"}') #works
print(data)    
data = parse_json('not json data at all') #throws error, the problem is with the json data, it should be in key value pairs
print(data) 