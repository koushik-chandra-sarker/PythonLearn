print("------------if statement------------")

x = 5
if x > 4:
    print("x is greater then 4")

print("------------if-else statement------------")

age = 15
if age >= 18:
    print("You are eligible to vote !!")
else:
    print("You aren't eligible to vote !!")

print("------------elif statement------------")

mark = 75  # Output: Grade: A
if 80 <= mark <= 100:
    print("Grade: A+")
elif 75 <= mark < 80:
    print("Grade: A")
elif 70 <= mark < 75:
    print("Grade: A-")
elif 65 <= mark < 70:
    print("Grade: B+")
elif 60 <= mark < 65:
    print("Grade: B")
elif 55 <= mark < 60:
    print("Grade: B-")
elif 50 <= mark < 55:
    print("Grade: C")
else:
    print("Failed")
