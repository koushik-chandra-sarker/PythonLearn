"""
Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it.

        A variable name must start with a letter or the underscore character
        A variable name cannot start with a number
        A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
        Variable names are case-sensitive (age, Age and AGE are three different variables)

        Illegal variable names:
             1variable = 13
             var-iable = 10
             var iable = 14

        Legal variable names:
            variable = 13
            my_name = "Koushik Chandra Sarker"
            myName = "Koushik Chandra Sarker"
            MYNAME = "Koushik Chandra Sarker"
            MYNAME2 = "Koushik Chandra Sarker"

"""

# Variables do not need to be declared with any particular type, and can even change type after they have been set.

x = 10  # int
x1 = 10.4  # float
y = "Hello Python"  # String-> str

print(x)  # Output: 10
print(type(x))  # Output: <class 'int'>

print(x1)  # Output: 10.4
print(type(x1))  # Output: <class 'float'>

print(y)  # Output: Hello Python
print(type(y))  # Output: <class 'str'>

# Case-Sensitive
#           Variable names are case-sensitive.

a = 13
A = 15

print(a)  # Output: 13
print(A)  # Output: 15


# Casting
# If you want to specify the data type of a variable, this can be done with casting.

a1 = str(a)
a2 = float(a)
print(type(a1))  # Output: <class 'str'>
print(type(a2))  # Output: <class 'float'>



"""
Python allows you to assign values to multiple variables in one line:
"""

a, b, c = "Red", "Green", "Yellow"

print(a)  # Output: Red
print(b)  # Output: Green
print(c)  # Output: Yellow

"""
you can assign the same value to multiple variables in one line:
"""

a = b = c = 10

print(a)  # Output: 10
print(b)  # Output: 10
print(c)  # Output: 10


