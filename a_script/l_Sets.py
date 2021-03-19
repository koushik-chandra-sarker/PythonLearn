"""
Sets are used to store multiple items in a single variable.
Sets are written with curly brackets.
Sets return an arbitrary element
"""

set1 = {"a", "b", "d", "c"}
set2 = {"abc", 34, True, 40, "male"}

print(set1)  # Output: ('a', 'b', 'd', 'c')
print(set2)  # Output: ("abc", 34, True, 40, "male")

print("-------------------Add Set Items--------------------")

set1.add("e")
print(set1)  # Output: {'b', 'd', 'a', 'c', 'e'}

# Add Sets
# To add items from another set into the current set, use the update() method.

set1.update(set2)
print(set1)  # Output: {'a', True, 34, 'd', 40, 'e', 'male', 'c', 'abc', 'b'}

print("-------------------Remove Set Items--------------------")
# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.


# remove()
#  If the item to remove does not exist, remove() will raise an error.
set1 = {"a", "b", "d", "c"}
set1.remove("d")
print(set1)  # Output: {'a', 'c', 'b'}

# discard()
# If the item to remove does not exist, discard() will NOT raise an error.
set1 = {"a", "b", "d", "c"}
set1.discard("a")
print(set1)  # Output: {'c', 'b', 'd'}

# pop()
# Remove and return an arbitrary element from the set.
set1 = {"a", "b", "d", "c"}
set1.pop()
print(set1)  # Output: {'a', 'd', 'c'}

# The clear() method empties the set:
set1 = {"a", "b", "d", "c"}
set1.clear()
print(set1)  # Output: set()

# The del keyword will delete the set completely:

set1 = {"a", "b", "d", "c"}
del set1
# print(set1)  # NameError: name 'set1' is not defined

"""Loops are as same Lists see Lists_Loop"""

print("------------------Join Sets Items--------------------")

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)  # Output: {1, 2, 3, 'b', 'a', 'c'}

set1 = {"aa", "bb", "cc"}
set2 = {"bb", "dd", "ee"}

set1.intersection_update(set2)
print(set1)  # Output: {'bb'}

set1 = {"aa", "bb", "cc"}
set2 = {"bb", "dd", "ee"}

set3 = set1.intersection(set2)
print(set3)  # Output: {'bb'}

# Keep All, But NOT the Duplicates

set1 = {"aa", "bb", "cc"}
set2 = {"bb", "dd", "ee"}

set1.symmetric_difference_update(set2)
print(set1)  # Output: {'aa', 'cc', 'dd', 'ee'}

set1 = {"aa", "bb", "cc"}
set2 = {"bb", "dd", "ee"}

set3 = set1.symmetric_difference(set2)
print(set3)  # Output: {'aa', 'cc', 'dd', 'ee'}
