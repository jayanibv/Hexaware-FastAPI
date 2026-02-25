import json
#''' - means commented, but here it executes cuz it is considered as a string, which isn't assigned to any variable
#multiple line string, response has this json data
response='''
{
"order_id": 1001,
"customer": {"name": "John", 
"email": "john@example.com"
},
"items": [
    {"product": "Laptop", "qty": 1,"price": 1200},
    {"product": "Mouse", "qty": 2,"price": 20}
]
}
'''
order=json.loads(response) #json.loads() -> JSON string to Python dict
print(order["items"][0]["product"])
print(order["customer"]["name"])

for item in order["items"]:
    total=item['qty']*item['price']
    print(f"{item['product']} Total: {total}")