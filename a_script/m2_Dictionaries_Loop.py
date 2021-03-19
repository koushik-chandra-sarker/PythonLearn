user = {
    "username": "koushikStack",
    "password": 1234,
    "active": True
}
print("------------ Print all key names --------------")
# Print all key names in the dictionary, one by one:
for u in user:
    print(u)
    """
    # Output:
            username
            password
            active
    """
print("------------ Print all key names using the keys() method--------------")
# Print all key names in the dictionary, one by one:
for u in user.keys():
    print(u)
    """
    # Output:
            username
            password
            active
    """

print("------------ Print all values --------------")

# Print all values in the dictionary, one by one:
for u in user:
    print(user[u])
    """
        # Output:
                koushikStack
                1234
                True
    """

print("------------ Print all values use the values() method--------------")
# You can also use the values() method to return values of a dictionary:
for u in user.values():
    print(u)
    """
        # Output:
                koushikStack
                1234
                True
    """

print("------------ Loop through both keys and values, by using the items() method:--------------")

for k, v in user.items():
    print(k, ":", v)
    """
        # Output:
                username : koushikStack
                password : 1234
                active : True
    """
