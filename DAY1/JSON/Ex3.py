#to read a json file
import json
with open("user.json","r") as file:
    data=json.load(file)
    print(data)

print(data["name"]+" is from "+data["city"])
#print(data["age"])
#print(data["age"]+"5") #this will throw error, can't add int and str
print(int(data["age"]) + 5) #this will work
print(data["name"]+ "Jays")