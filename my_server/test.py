from pprint import pprint

users = []

data = {'name' : 123, "email" : "asdasdasd@asdasd"}
users.append(data)
data = {'name' : 23, "email" : "asdas@asdasd"}
users.append(data)
data = {'name' : "asdas", "email" : "adia@gmail.com"}
users.append(data)


name_to_remove = data['name']  # The last added data['name'], i.e., "asdas"

# Check if the name exists in the list of dictionaries
if any(user["name"] == name_to_remove for user in users):
    pprint(users)  # Print before deletion
    users = [user for user in users if user["name"] != name_to_remove]
    pprint(users)  # Print after deletion
else:
    print("User not exists")
