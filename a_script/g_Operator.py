"""
Python divides the operators in the following groups:

    -> Arithmetic operators
    -> Assignment operators
    -> Comparison operators
    -> Logical operators
    -> Identity operators
    -> Membership operators
    -> Bitwise operators

             ---------- Arithmetic operators----------
        Operator	    Name	            Example
            +	    Addition	            x + y
            -	    Subtraction 	        x - y
            *	    Multiplication      	x * y
            /	    Division	            x / y
            %	    Modulus	                x % y
            **	    Exponentiation	        x ** y
            //	    Floor division	        x // y

            ---------- Assignment operators----------
            Operator	            Example	            Same As
                =	                x = 5	            x = 5
                +=	                x += 3	            x = x + 3
                -=	                x -= 3	            x = x - 3
                *=	                x *= 3	            x = x * 3
                /=	                x /= 3	            x = x / 3
                %=	                x %= 3	            x = x % 3
                //=	                x //= 3	            x = x // 3
                **=	                x **= 3	            x = x ** 3
                &=	                x &= 3	            x = x & 3
                |=	                x |= 3	            x = x | 3
                ^=	                x ^= 3	            x = x ^ 3
                >>=	                x >>= 3	            x = x >> 3
                <<=	                x <<= 3	            x = x << 3

               ---------- Comparison operators----------
                  Operator	        Name	                            Example

                    ==	            Equal	                            x == y
                    !=	            Not equal	                        x != y
                    >	            Greater than	                    x > y
                    <	            Less than	                        x < y
                    >=	            Greater than or equal to	        x >= y
                    <=	            Less than or equal to	            x <= y

               ---------- Logical operators----------
            Operator	           Description	                                                  Example

             and 	           Returns True if both statements are true	                    x < 5 and  x < 10
             or	               Returns True if one of the statements is true	            x < 5 or x < 4
             not	               Reverse the result, returns False if the result is true	   not(x < 5 and x < 10)



              ----------Identity Operators----------
        Operator	                Description	                                                     Example

          is 	                    Returns True if both variables are the same object	            x is y
          is not	                Returns True if both variables are not the same object	        x is not y



              ----------Membership Operators----------
        Operator	        Description	                                            Example

          in 	            Returns True if a sequence with the specified
                          value is present in the object	                        x in y

          not in	        Returns True if a sequence with the specified
                          value is not present in the object	                    x not in y

            ----------Bitwise Operators----------
        Operator	    Name	            Description

        & 	            AND	                Sets each bit to 1 if both bits are 1
        |	            OR	                Sets each bit to 1 if one of two bits is 1
         ^	            XOR	                Sets each bit to 1 if only one of two bits is 1
        ~ 	            NOT	                Inverts all the bits
        <<	            'Zero fill 	        Shift left by pushing zeros in
                        left shift'          from the right and let the leftmost bits fall off

        >>	            'Signed              Shift right by pushing copies of the leftmost bit
                        right shift'         in from the left, and let the rightmost bits fall off


"""

print("---------- Arithmetic operators----------")

print(2 + 5)  # Output: 7
print(5 - 2)  # Output: 3
print(5 * 2)  # Output: 10
print(10 / 2)  # Output: 5
print(11 % 2)  # Output: 1
print(4 ** 2)  # Output: 16
print(5 / 2)  # Output: 2.5
print(4 // 2)  # Output: 1

print("---------- Assignment operators----------")

x = 5
print(x)  # Output: 5
x += 2
print(x)  # Output: 7
x -= 2
print(x)  # Output: 5
x1 = 4
x1 *= 2
print(x1)  # Output: 8

x1 = 6
x1 /= 2
print(x1)  # Output: 3.0

x1 = 7
x1 %= 2
print(x1)  # Output: 1

x1 = 7
x1 //= 2
print(x1)  # Output: 3
x1 = 4
x1 **= 2
print(x1)  # Output: 16
x1 = 0
x1 &= 1
print(x1)  # Output: 0

x1 = 1
x1 |= 0
print(x1)  # Output: 1

print("---------- Comparison Operators ----------")

print(5 == 5)  # Output: True
print(5 == 4)  # Output: False
print(5 == "5")  # Output: False
print(5 != 3)  # Output: True
print(5 != 5)  # Output: False
print(5 > 4)  # Output: True
print(5 < 4)  # Output: False
print(5 >= 6)  # Output: False
print(5 >= 5)  # Output: True
print(5 >= 4)  # Output: True

print(5 <= 6)  # Output: True
print(5 <= 5)  # Output: True
print(5 <= 4)  # Output: False

print("---------- Logical Operators ----------")

x = 5
print(x > 3 and x < 10)  # Output: Ture
print(x > 3 and x < 4)  # Output: False

print(x > 3 or x < 4)  # Output: True
print(x > 3 or x < 10)  # Output: True
print(x > 5 or x < 4)  # Output: False

print(not True)  # Output: False
print(not (x > 3 or x < 4))  # Output: False

print("---------- Identity Operators ----------")

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
"""  --------- is ---------"""
print(x is z)  # Output: True

# returns True because z is the same object as x

print(x is y)  # Output: False

# returns False because x is not the same object as y, even if they have the same content

print(x == y)  # Output: True

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

"""  --------- is not ---------"""
print(x is not z)  # Output: False

# returns False because z is the same object as x

print(x is not y)  # Output: True

# returns True because x is not the same object as y, even if they have the same content

print(x != y)  # Output: False

# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y


print("---------- Membership Operators ----------")

print("banana" not in x)  # Output: False
print("bana" not in x)  # Output: True
