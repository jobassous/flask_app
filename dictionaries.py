person = {"name": "Nathan", "age": 68, "height": 5 * 12 + 10 }

print(person)

print(person["name"])

person["city"] = "New York"
print(person["city"])
print(person)

for key, value in person.items():
	print("The key is: {} and the value is: {}".format(key, value))