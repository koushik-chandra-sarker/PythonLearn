"""
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

Example:

Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

Without list comprehension you will have to write a for statement with a conditional test inside:

"""

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = []

for x in fruits:
    if "a" in x:
        newList.append(x)

print(newList)  # Output: ['apple', 'banana', 'mango']

# With list comprehension you can do all that with only one line of code:

newList = [x for x in fruits if "a" in x]
print(newList)  # Output: ['apple', 'banana', 'mango']


newList = [x for z in fruits if z != "apple"]
print(newList)  # Output: ['banana', 'cherry', 'kiwi', 'mango']

# With no if statement:
newList = [x for x in fruits]
print(newList)  # Output: ['apple', 'banana', 'cherry', 'kiwi', 'mango']

# range()
newList = [x for x in range(10)]
print(newList)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

newList = [x for z in range(10) if z < 5]
print(newList)  # Output: [0, 1, 2, 3, 4]

# Convert all to upper case
newList = [x.upper() for x in fruits]
print(newList)  # Output: ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

# Return one instead of anther:
# Return "orange" instead of "banana":
newList = [x if x != "banana" else "orange" for x in fruits]
print(newList)  # Output: ['apple', 'orange', 'cherry', 'kiwi', 'mango']
