"""
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
Dictionaries are written with curly brackets, and have keys and values:
"""

user = {
    "username": "koushikStack",
    "password": 1234,
    "active": True
}
print(user)  # Output: {'username': 'koushikStack', 'password': 1234, 'active': True}

print(user["username"])  # Output: koushikStack

# Duplicates Not Allowed
user = {
    "username": "koushikStack",
    "password": 1234,
    "active": True,
    "active": False
}

print(user)  # Output: {'username': 'koushikStack', 'password': 1234, 'active': False}

# Length
# Duplicates Not counted
print(len(user))  # Output: 3

user = {
    "username": "koushikStack",
    "password": 1234,
    "active": True,
    "phone": ["01622222222", "01711111111"]
}
print(user)
# Output: {'username': 'koushikStack', 'password': 1234, 'active': True, 'phone': ['01622222222', '01711111111']}


print("------------------Accessing Items---------------------")

uname = user['username']
print(uname)  # Output: koushikStack

password = user.get("password")

print(password)  # Output: 1234

print(user.keys())  # Output: dict_keys(['username', 'password', 'active', 'phone'])

# Get Values
# The values() method will return a list of all the values in the dictionary.

print(user.values())  # Output: dict_values(['koushikStack', 1234, True, ['01622222222', '01711111111']])

# Get Items
# The items() method will return each item in a dictionary, as tuples in a list.

print(user.items())
"""
# Output: 
dict_items([('username', 'koushikStack'), ('password', 1234), ('active', True),
            ('phone', ['01622222222', '01711111111'])])
"""

print("------------------Change Values---------------------")

user = {
    "username": "koushikStack",
    "password": 1234,
    "active": True
}
user["password"] = 1111

print(user)  # Output:  {'username': 'koushikStack', 'password': 1111, 'active': True}

user.update({"active": False})
print(user)  # Output:  {'username': 'koushikStack', 'password': 1111, 'active': False}

print("------------------Change Values---------------------")

user["email"] = "aaa@gmail.com"
print(user)  # Output:  {'username': 'koushikStack', 'password': 1111, 'active': False, 'email': 'aaa@gmail.com'}

user.update({"name": "Koushik"})
print(user)
# Output:  {'username': 'koushikStack', 'password': 1111, 'active': False, 'email': 'aaa@gmail.com', 'name': 'Koushik'}

print("------------------Removing Items---------------------")

user.pop("name")
print(user)  # Output:  {'username': 'koushikStack', 'password': 1111, 'active': False, 'email': 'aaa@gmail.com'}

# The popitem() method removes the last inserted item
user.popitem()
print(user)  # Output:  {'username': 'koushikStack', 'password': 1111, 'active': False}

# The del keyword removes the item with the specified key name:

del user["active"]
print(user)  # Output:  {'username': 'koushikStack', 'password': 1111}

# The del keyword can also delete the dictionary completely:

del user
# print(user)  # NameError: name 'user' is not defined

user = {
    "username": "koushikStack",
    "password": 1234,
    "active": True
}
user.clear()
print(user)  # Output: {}

print("------------------Copy Dictionaries---------------------")
user = {
    "username": "koushikStack",
    "password": 1234,
    "active": True
}
newUser = user.copy()
print(newUser)  # Output: {'username': 'koushikStack', 'password': 1234, 'active': True}

# or
newUser1 = dict(user)
print(newUser1)  # Output: {'username': 'koushikStack', 'password': 1234, 'active': True}

