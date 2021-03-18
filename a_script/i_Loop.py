"""
Python has two primitive loop commands:
    -> while loops
    -> for loops
"""

print("-----------while Loops-----------")
i = 1
while i < 10:
    print(i, end=" ")  # Output: 1 2 3 4 5 6 7 8 9  # {end} keyword for print without newline
    i += 1

print()

i = 1
while i < 10:
    print(i, end=" ")  # Output: 1 2 3 4 5
    if i == 5:
        break
    i += 1

print()
print("-----------for Loops-----------")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

print("-----------for Loops Range() function-----------")
# he range() function defaults to 0 as a starting value

for i in range(5):  # Note that range(5) is not the values of 0 to 5, but the values 0 to 4.
    print(i, end=" ")  # Output: 0 1 2 3 4

print()
# Using the start parameter:
for i in range(3, 10):
    print(i, end=" ")  # Output: 3 4 5 6 7 8 9

# Increment the sequence with 2 (default is 1):
print()
for i in range(2, 10, 2):
    print(i, end=" ")  # Output: 2 4 6 8

# Else in For Loop
print()
for i in range(5):
    print(i, end=" ")  # Output: 0 1 2 3 4
else:
    print("Finished.")

# Nested Loops
for i in range(1, 6):
    for j in range(1, i+1):
        print("*", end=" ")
    print()
"""
Output:
        * 
        * * 
        * * * 
        * * * * 
        * * * * * 
"""

# break statement

