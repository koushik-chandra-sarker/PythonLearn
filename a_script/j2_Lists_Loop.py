list1 = ["Cat", 'Dog', "Rabbit", "Duck, Shrimp", "Pig"]


print("-------------Loop Through a List-------------")
for i in list1:
    print(i)
"""
Output:
        Cat
        Dog
        Rabbit
        Duck, Shrimp
        Pig
"""
print("-------------Loop Through the Index Numbers-------------")

for i in range(len(list1)):
    print(list1[i])

"""
Output:
        Cat
        Dog
        Rabbit
        Duck, Shrimp
        Pig
"""