"""
sort() method that will sort the list alphanumerically, ascending, by default:
"""

print("--------Sort the list alphabetically:-----------")

list1 = ["bb", "ss", "dd", "aa", "cc"]
list1.sort()
print(list1)  # Output: ['aa', 'bb', 'cc', 'dd', 'ss']

print("--------Sort the list numerically: ascending-----------")

list1 = [5, 4, 10, 1, 25, 2]
list1.sort()
print(list1)  # Output: [1, 2, 4, 5, 10, 25]

print("--------Sort the list numerically: Descending-----------")

# Sort Descending
list1 = [5, 4, 10, 1, 25, 2]
list1.sort(reverse=True)
print(list1)  # Output: [25, 10, 5, 4, 2, 1]

"""
By default the sort() method is case sensitive,
"""

# Case sensitive sorting can give an unexpected result:
list1 = ["bb", "Ss", "dd", "Aa", "cc"]
list1.sort()
print(list1)  # Output: ['Aa', 'Ss', 'bb', 'cc', 'dd']
