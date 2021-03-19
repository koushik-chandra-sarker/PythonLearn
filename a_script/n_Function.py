"""
A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.

There are the following advantages of Python functions.

        -> Using functions, we can avoid rewriting the same logic/code again and again in a program.
        -> We can call Python functions multiple times in a program and anywhere in a program.
        -> We can track a large Python program easily when it is divided into multiple functions.
        -> Reusability is the main achievement of Python functions.
        -> However, Function calling is always overhead in a Python program.
"""


# Python provides the {def} keyword to define the function.

def Greeting():
    print("Welcome Python Function")


# Calling Function
Greeting()

"""
Arguments
Information can be passed into functions as arguments.
We can pass any number of arguments, but they must be separate them with a comma.
"""


# Parameter with return statement
def sum(a, b):  # a and b are Parameter
    c = a + b
    return c


d = sum(5, 3)  # 5 and 3 are Argument
print(d)  # Output: 8


# Default Arguments
def sub(value, x=3):
    return value - x


s = sub(10)
print(s)  # Output: 7

s = sub(10, 5)
print(s)  # Output: 5


# Variable-length(Arbitrary) Arguments (*args)

def display(*value):
    print(value)


display("Hello", "Python")  # Output: ('Hello', 'Python')
display(1, 5, 3, 5)  # Output: 1, 5, 3, 5)


# Keyword Arguments
# You can also send arguments with the key = value syntax.

def mul(a, b):
    print("Multiplication of %d & %d =" % (a, b), a + b)


mul(a=10, b=4)  # Output:Multiplication of 10 & 4 = 14
