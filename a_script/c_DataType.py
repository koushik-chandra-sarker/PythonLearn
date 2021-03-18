"""
Python has the following data types built-in by default, in these categories:

    Text Type:	str
    Numeric Types:	int, float, complex
    Sequence Types:	list, tuple, range
    Mapping Type:	dict
    Set Types:	set, frozenset
    Boolean Type:	bool
    Binary Types:	bytes, bytearray, memoryview

"""

x1 = "Hello Python"  # Data Type: str
print("Type of x1: ", type(x1))  # Output: Type of x1:  <class 'str'>

x2 = 12  # Data Type: int
print("Type of x2: ", type(x2))  # Output: Type of x2:  <class 'int'>

x3 = 12.5  # Data Type: float
print("Type of x3: ", type(x3))  # Output: Type of x3:  <class 'float'>

x4 = 5j  # Data Type: complex
print("Type of x4: ", type(x4))  # Output: Type of x4:  <class 'complex'>

x5 = [23, 34, 23, 22]  # Data Type: list
print("x5:", x5)  # Output: x5: [23, 34, 23, 22]
print("x5[3]:", x5[3])  # Output: x5[3]: 22
print("Type of x5: ", type(x5))  # Output: Type of x5:  <class 'list'>

x6 = (23, 34, 23, 22)  # Data Type: list
print("x6:", x6)  # Output: x6: [23, 34, 23, 22]
print("x6[3]:", x6[2])  # Output: x6[3]: 23
print("Type of x6: ", type(x6))  # Output: Type of x6:  <class 'list'>

x7 = range(10)
print(x7)  # Output: x6: range(0, 10)
print("Type of x7: ", type(x7))  # Output: Type of x7:  <class 'range'>

x8 = {23, 34, 23, 22}  # Data Type: set
print("Type of x6: ", type(x8))  # Output: Type of x8:  <class 'set'>

x9 = {"Name": "Koushik", "Age": 23}  # Data Type: dist
print("Type of x9: ", type(x9))  # Output: Type of x9:  <class 'dist'>

x10 = frozenset({"apple", "banana", "cherry"})
print("Type of x10: ", type(x10))  # Output: Type of x10:  <class 'frozenset'>

x11 = True
print("Type of x11: ", type(x11))  # Output: Type of x11: <class 'bool'>

x12 = b"Hello Python"
print("Type of x12: ", type(x12))  # Output: Type of x12: <class 'bytes'>

x13 = bytearray(4)
print("Type of x13: ", type(x13))  # Output: Type of x13: <class 'bytearray'>

x14 = memoryview(bytes(5))
print("Type of x14: ", type(x14))  # Output: Type of x14: <class 'memoryview'>

# Setting the Specific Data Type

a = str("Hello")
a = int(10)
a = float(10.2)
a = complex(2j)
a = list(("apple", "banana", "cherry"))
a = tuple(("apple", "banana", "cherry"))
a = range(6)
a = dict(name="John", age=36)
a = set(("apple", "banana", "cherry"))
a = frozenset(("apple", "banana", "cherry"))
a = bool(5)
a = bytes(5)
a = bytearray(5)
a = memoryview(bytes(5))





