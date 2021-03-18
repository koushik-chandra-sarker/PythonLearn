"""

Strings in python are surrounded by either single quotation marks, or double quotation marks.
Example: "Hello Python" or 'Hello Python'

"""

print("Hello Python -> Double quote")
print('Hello Python -> Single quote')

# Multiline Strings
#   You can assign a multiline string to a variable by using three quotes:

s = """Lorem ipsum dolor sit amet,
consecrated advising elite,
sed do emus temper incident
ut labor et door magna alia."""

s1 = '''Lorem ipsum dolor sit amet,
consecrated advising elite,
sed do emus temper incident
ut labor et door magna alia.'''

print(s)
print(s1)

# Length
print(len(s))

"""
Python does not have a character data type, a single character is simply a string with a length of 1
"""

# Strings are Arrays
print(s[1])  # Output: o

# Looping Through a String
for a in "Apple":
    print(a)
"""
Output:
        A
        p
        p
        l
        e
"""

# Check String
text = 'Hello Koushik, This is your first python practise'

print("first" in text)  # Output: True

if "Koushik" in text:
    print("Yes, 'Koushik' is present.")  # Output: Yes, 'Koushik' is present.

# Check if NOT
if "Sarker" not in text:
    print("Yes, 'Sarker' is Not present.")  # Output: Yes, 'Koushik' is Not present.

"""------------Slicing Strings------------"""

# You can return a range of characters by using the slice syntax.

# Get the characters from position 6 to position 13-1
print(text[6:13])  # Output: Koushik

# Slice From the Start
print(text[:13])  # Output: Hello Koushik

# Slice To the End
print(text[15:])  # Output: This is your first python practise

# Negative Indexing
print(text[-6:-2])  # Output: acti

"""------------Modify Strings------------"""

text2 = "Hello Python"

# Upper Case
print(text2.upper())  # Output: HELLO PYTHON

# Lower Case
print(text2.lower())  # Output: hello python

text3 = "   Hello Python    "

print(text3)  # Output: '   Hello Python    '

# Remove Whitespace
print(text3.strip())  # Output: 'Hello Python'

# Replace String

print(text2.replace("Hello", "Hi"))  # Output:Hi Python

# Split String
t = "abc, def"
print(t.split(','))  # Output: ['abc', ' def']

# Concatenation
t1 = 'abc'
t2 = 'efg'
# To concatenate, or combine, two strings you can use the + operator.
print(t1 + t2)  # Output: abcefg

# To add a space between them, add t1 " ":
print(t1 + ' ' + t2)  # Output: abc efg

"""----------Format----------"""
a = 24
"""
print(" a =" + a) # Through an error
"""
a1 = " a = {}"
print(a1.format(a))  # Output: a = 24

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))  # Output: I want 3 pieces of item 567 for 49.95 dollars.

myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))  # Output: I want to pay 49.95 dollars for 3 pieces of item 567.

""" 
 String Methods Reference:
        https://docs.python.org/3.8/library/stdtypes.html#string-methods 
        or
        https://www.w3schools.com/python/python_ref_string.asp
"""
