"""
A list in Python is used to store the sequence of various types of data.
Lists are created using square brackets:
"""
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = ["Apple", "Orange", "Banana"]
list3 = ["abc", 34, True, 40, "male"]

# The list() Constructor
list4 = list(("apple", "banana", "cherry"))  # note the double round-brackets
print(list4)  # Output: ['apple', 'banana', 'cherry']

print(list1[2])  # Output: 3

# Range of Indexes
# This example returns the items from index 2 to the end:
print(list1[2:])  # Output:[3, 4, 5, 6, 7, 8, 9]

# This example returns the items from the beginning to index 5-1
print(list1[:5])  # Output: [3, 4, 5]

print(list1[2:5])  # Output: [3, 4, 5]
print(list1[1:6:2])  # Output: [2, 4, 6]

print(list1[-1])  # Output: 9
print(list1[-3:])  # Output: [7, 8, 9]
print(list1[:-1])  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
print(list1[-3:-1])  # Output: [7, 8]

print("-------Change List Items----------")

list5 = ["Apple", "Orange", "Banana"]
list5[1] = "cherry"
print(list5)  # Output: ['Apple', 'cherry', 'Banana']

# Change a Range of Item Values

list6 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
list6[1:3] = ["blackcurrant", "watermelon"]
print(list6)  # Output: ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

print("-------Add List Items----------")

# Append Items
list8 = ["apple", "banana", "cherry"]
list8.append("orange")
print(list8)  # Output: ['apple', 'banana', 'cherry', 'orange']

# Insert Items
list9 = ["apple", "banana", "cherry"]
list9.insert(1, "orange")
print(list9)  # Output: ['apple', 'orange', 'banana', 'cherry']

# Extend List
list10 = ["apple", "banana", "cherry"]
list11 = ["mango", "pineapple", "papaya"]
list10.extend(list11)
print(list10)  # Output:['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

# Add Any Iterable
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
list12 = ["apple", "banana", "cherry"]
tuple1 = ("kiwi", "orange")
list12.extend(tuple1)
print(list12)  # Output: ['apple', 'banana', 'cherry', 'kiwi', 'orange']

print("-------Remove List Items----------")

# Remove Specified Item
list13 = ["apple", "banana", "cherry"]
list13.remove("banana")
print(list13)  # Output:['apple', 'cherry']

# Remove Specified Index
list13 = ["apple", "banana", "cherry"]
list13.pop(2)
print(list13)  # Output:['apple', 'banana']

# If you do not specify the index, the pop() method removes the last item.
list13 = ["apple", "banana", "cherry"]
list13.pop()
print(list13)  # Output:['apple', 'banana']

# The {del} keyword can also delete the list completely.
list13 = ["apple", "banana", "cherry"]
del list13
# print(list13)  # NameError: name 'list13' is not defined

# Clear the List
list13 = ["apple", "banana", "cherry"]
list13.clear()
print(list13)  # Output:[]
