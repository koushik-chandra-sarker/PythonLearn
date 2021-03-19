"""
Python Built-in Functions:  https://docs.python.org/3/library/functions.html
                            or https://www.javatpoint.com/python-built-in-functions

"""

# abs()
# abs() function is used to return the absolute value of a number.
i = -12
print("Absolute value of -40 is:", abs(i))  # Output: Absolute value of -40 is: 12

# bin()
# Convert an integer number to a binary string prefixed with “0b”.
i = 5
print(bin(i))  # Output: 0b101

# sum()
x = sum([2, 5, 3])
print(x)  # Output: 10

x = sum((5, 5, 3))
print(x)  # Output: 13

x = sum((5, 5, 3), 10)
print(x)  # Output: 23

x = sum((3 + 5j, 4 + 3j))
print(x)  # Output: (7+8j)

# pow()
"""
pow(x, y, z)  

x: It is a number, a base

y: It is a number, an exponent.

z (optional): It is a number and the modulus.
"""

print(pow(2, 3))  # Output: 8
print(pow(4, 2))  # Output: 16
print(pow(-4, 2))  # Output: 16
print(pow(-2, 3))  # Output: -8

#  min() function is used to get the smallest element from the collection.

s = min(123, 2, 5, 3, 6, 35)
print(s)  # Output: 2

s = min([10, 12], [12, 21], [13, 15])
print(s)  # Output: 2[10, 12]

s = min("Python", "Java", "Scala")
print(s)  # Output: java

s = min([10, 12, 33], [12, 21, 55], [13, 15], key=len)
print(s)  # Output:[13,15]

#  max() function is used to get the highest element from the collection.

s = max(123, 2, 5, 3, 6, 35)
print(s)  # Output: 123

s = max([10, 12], [12, 21], [13, 15])
print(s)  # Output: [13, 15]

s = max("Python", "Java", "Scala")
print(s)  # Output: scala

s = max([10, 12, 33], [12, 21, 55, 9], [13, 15], key=len)
print(s)  # Output:[12, 21, 55, 9]
