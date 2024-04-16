add()	Elements can be added to a set using the `add()` method. Duplicates are automatically removed, as sets only store unique values.	Syntax:
1
set_name.add(element) 
Copied!
Example:

1
fruits.add("mango")
Copied!
clear()	The `clear()` method removes all elements from the set, resulting in an empty set. It updates the set in-place.	Syntax:
1
set_name.clear() 
Copied!
Example:

1
fruits.clear()
Copied!
copy()	The `copy()` method creates a shallow copy of the set. Any modifications to the copy won't affect the original set.	Syntax:
1
new_set = set_name.copy() 
Copied!
Example:

1
new_fruits = fruits.copy()
Copied!
Defining Sets	A set is an unordered collection of unique elements. Sets are enclosed in curly braces `{}`. They are useful for storing distinct values and performing set operations.	Example:
1
2
empty_set = set() #Creating an Empty Set 
fruits = {"apple", "banana", "orange"}
Copied!
discard()	Use the `discard()` method to remove a specific element from the set. Ignores if the element is not found.	Syntax:
1
set_name.discard(element) 
Copied!
Example:

1
fruits.discard("apple")
Copied!
issubset()	The `issubset()` method checks if the current set is a subset of another set. It returns True if all elements of the current set are present in the other set, otherwise False.	Syntax:
1
is_subset = set1.issubset(set2) 
Copied!
Example:

1
is_subset = fruits.issubset(colors)
Copied!
issuperset()	The `issuperset()` method checks if the current set is a superset of another set. It returns True if all elements of the other set are present in the current set, otherwise False.	Syntax:
1
is_superset = set1.issuperset(set2) 
Copied!
Example:

1
is_superset = colors.issuperset(fruits)
Copied!
pop()	The `pop()` method removes and returns an arbitrary element from the set. It raises a `KeyError` if the set is empty. Use this method to remove elements when the order doesn't matter.	Syntax:
1
removed_element = set_name.pop() 
Copied!
Example:

1
removed_fruit = fruits.pop()
Copied!
remove()	Use the `remove()` method to remove a specific element from the set. Raises a `KeyError` if the element is not found.	Syntax:
1
set_name.remove(element) 
Copied!
Example:

1
fruits.remove("banana")
Copied!
Set Operations	Perform various operations on sets: `union`, `intersection`, `difference`, `symmetric difference`.	Syntax:
1
2
3
4
union_set = set1.union(set2)
intersection_set = set1.intersection(set2) 
difference_set = set1.difference(set2) 
sym_diff_set = set1.symmetric_difference(set2)
Copied!
Example:

1
2
3
4
combined = fruits.union(colors) 
common = fruits.intersection(colors) 
unique_to_fruits = fruits.difference(colors) 
sym_diff = fruits.symmetric_difference(colors)
Copied!
update()	The `update()` method adds elements from another iterable into the set. It maintains the uniqueness of elements.	Syntax:
1
set_name.update(iterable) 
Copied!
Example:

1
fruits.update(["kiwi", "grape"]
