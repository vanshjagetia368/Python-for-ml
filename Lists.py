#================================================================================
# COMPREHENSIVE PYTHON LISTS TUTORIAL - COMPLETE GUIDE
#================================================================================
# What are Lists?
# Lists are one of the most fundamental data structures in Python that store an 
# ordered collection of items. They are defined using square brackets [] and can 
# contain items of different data types, including other lists (nested lists).
#
# KEY CHARACTERISTICS OF LISTS:
# - MUTABLE: You can change their contents after creation (add, remove, modify)
# - ORDERED: Elements maintain their position (index-based access)
# - DYNAMIC: Can grow or shrink in size as needed
# - INDEXABLE: Access elements using integer indices (0-based)
# - ITERABLE: Can loop through all elements
# - ALLOWS DUPLICATES: Same value can appear multiple times
# - HETEROGENEOUS: Can store different data types in the same list
#================================================================================

print("=" * 80)  # OUTPUT: ================================================================================
print("1. CREATING AND INITIALIZING LISTS")  # OUTPUT: 1. CREATING AND INITIALIZING LISTS
print("=" * 80)  # OUTPUT: ================================================================================

# Method 1: Creating a simple list with integer values
numbers = [1, 2, 3, 4, 5]
print(f"Simple integer list: {numbers}")  # OUTPUT: Simple integer list: [1, 2, 3, 4, 5]
print(f"Type: {type(numbers)}, Length: {len(numbers)}")  # OUTPUT: Type: <class 'list'>, Length: 5

# Method 2: Creating a list with mixed data types
mixed_list = [1, 2, 3, "Hello", 4.5, True, None]
print(f"Mixed data types list: {mixed_list}")  # OUTPUT: Mixed data types list: [1, 2, 3, 'Hello', 4.5, True, None]
print(f"Length: {len(mixed_list)}")  # OUTPUT: Length: 7

# Method 3: Creating a nested list (list within a list)
nested_list = [1, 2, 3, "Hello", [4, 5, 6], [7, [8, 9]]]
print(f"Nested list: {nested_list}")  # OUTPUT: Nested list: [1, 2, 3, 'Hello', [4, 5, 6], [7, [8, 9]]]
print(f"Length: {len(nested_list)}")  # OUTPUT: Length: 6

# Method 4: Creating an empty list
empty_list = []
print(f"Empty list: {empty_list}, Length: {len(empty_list)}")  # OUTPUT: Empty list: [], Length: 0

# Method 5: Creating a list using the list() constructor
from_string = list("Python")
print(f"List from string: {from_string}")  # OUTPUT: List from string: ['P', 'y', 't', 'h', 'o', 'n']

# Method 6: Creating a list using range()
range_list = list(range(1, 6))
print(f"List from range(1, 6): {range_list}")  # OUTPUT: List from range(1, 6): [1, 2, 3, 4, 5]

# Method 7: List comprehension (most Pythonic way)
squares = [x**2 for x in range(1, 6)]
print(f"List comprehension (squares): {squares}")  # OUTPUT: List comprehension (squares): [1, 4, 9, 16, 25]

# Method 8: List with repeated elements
repeated = [0] * 5
print(f"Repeated elements: {repeated}")  # OUTPUT: Repeated elements: [0, 0, 0, 0, 0]

print("\n" + "=" * 80)  # OUTPUT: (blank line)
print("2. ACCESSING LIST ELEMENTS (INDEXING)")  # OUTPUT: ================================================================================
print("=" * 80)  # OUTPUT: 2. ACCESSING LIST ELEMENTS (INDEXING)

# Starting with a fresh list for demonstration
my_list = [10, 20, 30, 40, 50, 60, 70]
print(f"Current list: {my_list}")  # OUTPUT: ================================================================================
  # OUTPUT: Current list: [10, 20, 30, 40, 50, 60, 70]

# Accessing by positive index (0-based from left)
print(f"Element at index 0: {my_list[0]}")  # OUTPUT: Element at index 0: 10
print(f"Element at index 3: {my_list[3]}")  # OUTPUT: Element at index 3: 40
print(f"Element at index 6: {my_list[6]}")  # OUTPUT: Element at index 6: 70

# Accessing by negative index (counting from right, -1 is last)
print(f"Last element (index -1): {my_list[-1]}")  # OUTPUT: Last element (index -1): 70
print(f"Second last element (index -2): {my_list[-2]}")  # OUTPUT: Second last element (index -2): 60
print(f"First element from right (index -7): {my_list[-7]}")  # OUTPUT: First element from right (index -7): 10

# Using enumerate() to get index and value
print("\nEnumerate list:")  # OUTPUT: (blank line)
for index, value in enumerate(my_list):  # OUTPUT: Enumerate list:
    print(f"  Index {index}: {value}")  # OUTPUT: Index 0: 10, Index 1: 20, Index 2: 30, Index 3: 40, Index 4: 50, Index 5: 60, Index 6: 70

print("\n" + "=" * 80)  # OUTPUT: (blank line)
print("3. LIST SLICING (ADVANCED INDEXING)")  # OUTPUT: ================================================================================
print("=" * 80)  # OUTPUT: 3. LIST SLICING (ADVANCED INDEXING)

print(f"Original list: {my_list}")  # OUTPUT: ================================================================================
  # OUTPUT: Original list: [10, 20, 30, 40, 50, 60, 70]

# Basic slicing: list[start:end]
print(f"my_list[1:4] (indices 1, 2, 3): {my_list[1:4]}")  # OUTPUT: my_list[1:4] (indices 1, 2, 3): [20, 30, 40]
print(f"my_list[0:3] (first 3 elements): {my_list[0:3]}")  # OUTPUT: my_list[0:3] (first 3 elements): [10, 20, 30]
print(f"my_list[:3] (same as above): {my_list[:3]}")  # OUTPUT: my_list[:3] (same as above): [10, 20, 30]

# Slicing from index to end
print(f"my_list[3:] (from index 3 to end): {my_list[3:]}")  # OUTPUT: my_list[3:] (from index 3 to end): [40, 50, 60, 70]

# Slicing with step: list[start:end:step]
print(f"my_list[::2] (every 2nd element): {my_list[::2]}")  # OUTPUT: my_list[::2] (every 2nd element): [10, 30, 50, 70]
print(f"my_list[1::2] (every 2nd element starting from index 1): {my_list[1::2]}")  # OUTPUT: my_list[1::2] (every 2nd element starting from index 1): [20, 40, 60]

# Negative step reverses the list
print(f"my_list[::-1] (reversed list): {my_list[::-1]}")  # OUTPUT: my_list[::-1] (reversed list): [70, 60, 50, 40, 30, 20, 10]
print(f"my_list[5:1:-1] (indices 5,4,3,2 reversed): {my_list[5:1:-1]}")  # OUTPUT: my_list[5:1:-1] (indices 5,4,3,2 reversed): [60, 50, 40, 30]

# Slicing with negative indices
print(f"my_list[-4:-1] (last 4 elements except the last): {my_list[-4:-1]}")  # OUTPUT: my_list[-4:-1] (last 4 elements except the last): [40, 50, 60]
print(f"my_list[-3:] (last 3 elements): {my_list[-3:]}")  # OUTPUT: my_list[-3:] (last 3 elements): [50, 60, 70]

print("\n" + "=" * 80)  # OUTPUT: (blank line)
print("4. MODIFYING LISTS - ASSIGNMENT AND REPLACEMENT")  # OUTPUT: ================================================================================
print("=" * 80)  # OUTPUT: 4. MODIFYING LISTS - ASSIGNMENT AND REPLACEMENT

# Reset list for this section
my_list = [10, 20, 30, 40, 50, 60, 70]
print(f"Original list: {my_list}")  # OUTPUT: ================================================================================
  # OUTPUT: Original list: [10, 20, 30, 40, 50, 60, 70]

# Modifying a single element
my_list[0] = 100
print(f"After my_list[0] = 100: {my_list}")  # OUTPUT: After my_list[0] = 100: [100, 20, 30, 40, 50, 60, 70]

# Modifying a single element using negative index
my_list[-1] = 700
print(f"After my_list[-1] = 700: {my_list}")  # OUTPUT: After my_list[-1] = 700: [100, 20, 30, 40, 50, 60, 700]

# Modifying multiple elements using slice assignment
my_list[1:3] = [200, 300]
print(f"After my_list[1:3] = [200, 300]: {my_list}")  # OUTPUT: After my_list[1:3] = [200, 300]: [100, 200, 300, 40, 50, 60, 700]

# Replacing with more elements than original slice
my_list[3:5] = [400, 401, 402, 403]
print(f"After my_list[3:5] = [400, 401, 402, 403]: {my_list}")  # OUTPUT: After my_list[3:5] = [400, 401, 402, 403]: [100, 200, 300, 400, 401, 402, 403, 60, 700]

# Replacing with fewer elements than original slice
my_list[3:6] = [999]
print(f"After my_list[3:6] = [999]: {my_list}")  # OUTPUT: After my_list[3:6] = [999]: [100, 200, 300, 999, 403, 60, 700]

# Modifying with slice assignment and step
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list[::2] = [100, 200, 300, 400, 500]
print(f"After my_list[::2] = [100, 200, 300, 400, 500]: {my_list}")  # OUTPUT: After my_list[::2] = [100, 200, 300, 400, 500]: [100, 2, 200, 4, 300, 6, 400, 8, 500, 10]

print("\n" + "=" * 80)  # OUTPUT: (blank line)
print("5. CORE LIST METHODS - ADDING ELEMENTS")  # OUTPUT: ================================================================================
print("=" * 80)  # OUTPUT: 5. CORE LIST METHODS - ADDING ELEMENTS

# Reset list for this section
my_list = [10, 20, 30]
print(f"Starting list: {my_list}")  # OUTPUT: ================================================================================
  # OUTPUT: Starting list: [10, 20, 30]

# 5.1 append() - Adds a single item to the END of the list
my_list.append(40)
print(f"After append(40): {my_list}")  # OUTPUT: After append(40): [10, 20, 30, 40]

my_list.append([50, 60])
print(f"After append([50, 60]): {my_list} [Note: Added as nested list]")  # OUTPUT: After append([50, 60]): [10, 20, 30, 40, [50, 60]] [Note: Added as nested list]

# 5.2 insert() - Inserts an item at a SPECIFIED INDEX
my_list = [10, 20, 30, 40]
my_list.insert(1, 15)
print(f"After insert(1, 15): {my_list} [Inserted 15 at index 1]")  # OUTPUT: After insert(1, 15): [10, 15, 20, 30, 40] [Inserted 15 at index 1]

my_list.insert(0, 5)
print(f"After insert(0, 5): {my_list} [Inserted 5 at beginning]")  # OUTPUT: After insert(0, 5): [5, 10, 15, 20, 30, 40] [Inserted 5 at beginning]

my_list.insert(100, 999)
print(f"After insert(100, 999): {my_list} [Index out of range inserts at end]")  # OUTPUT: After insert(100, 999): [5, 10, 15, 20, 30, 40, 999] [Index out of range inserts at end]

# 5.3 extend() - Adds multiple items from an ITERABLE
my_list = [10, 20, 30]
my_list.extend([40, 50, 60])
print(f"After extend([40, 50, 60]): {my_list}")  # OUTPUT: After extend([40, 50, 60]): [10, 20, 30, 40, 50, 60]

my_list.extend([70])
print(f"After extend([70]): {my_list}")  # OUTPUT: After extend([70]): [10, 20, 30, 40, 50, 60, 70]

my_list.extend("XY")
print(f"After extend('XY'): {my_list} [String is iterable, added char by char]")  # OUTPUT: After extend('XY'): [10, 20, 30, 40, 50, 60, 70, 'X', 'Y'] [String is iterable, added char by char]

print("\n" + "=" * 80)  # OUTPUT: (blank line)
print("6. CORE LIST METHODS - REMOVING ELEMENTS")  # OUTPUT: ================================================================================
print("=" * 80)  # OUTPUT: 6. CORE LIST METHODS - REMOVING ELEMENTS

# 6.1 remove() - Removes FIRST OCCURRENCE of a value
my_list = [10, 20, 30, 20, 40, 20]
print(f"Starting list: {my_list}")  # OUTPUT: ================================================================================
  # OUTPUT: Starting list: [10, 20, 30, 20, 40, 20]

my_list.remove(20)
print(f"After remove(20): {my_list} [Removed first occurrence of 20]")  # OUTPUT: After remove(20): [10, 30, 20, 40, 20] [Removed first occurrence of 20]

my_list.remove(10)
print(f"After remove(10): {my_list}")  # OUTPUT: After remove(10): [30, 20, 40, 20]

# 6.2 pop() - Removes and returns an item at a SPECIFIED INDEX (default: last)
my_list = [10, 20, 30, 40, 50]
print(f"\nStarting list: {my_list}")  # OUTPUT: (blank line)
  # OUTPUT: Starting list: [10, 20, 30, 40, 50]

popped_item = my_list.pop()
print(f"Popped item: {popped_item}, List after pop(): {my_list}")  # OUTPUT: Popped item: 50, List after pop(): [10, 20, 30, 40]

popped_item = my_list.pop(1)
print(f"Popped item at index 1: {popped_item}, List after pop(1): {my_list}")  # OUTPUT: Popped item at index 1: 20, List after pop(1): [10, 30, 40]

popped_item = my_list.pop(0)
print(f"Popped item at index 0: {popped_item}, List after pop(0): {my_list}")  # OUTPUT: Popped item at index 0: 10, List after pop(0): [30, 40]

# 6.3 del statement - Deletes item(s) at a SPECIFIED INDEX or SLICE
my_list = [10, 20, 30, 40, 50, 60, 70]
print(f"\nStarting list: {my_list}")  # OUTPUT: (blank line)
  # OUTPUT: Starting list: [10, 20, 30, 40, 50, 60, 70]

del my_list[1]
print(f"After del my_list[1]: {my_list}")  # OUTPUT: After del my_list[1]: [10, 30, 40, 50, 60, 70]

del my_list[1:4]
print(f"After del my_list[1:4]: {my_list}")  # OUTPUT: After del my_list[1:4]: [10, 60, 70]

# 6.4 clear() - Removes ALL items from the list
my_list = [10, 20, 30, 40]
print(f"\nBefore clear(): {my_list}")  # OUTPUT: (blank line)
  # OUTPUT: Before clear(): [10, 20, 30, 40]
my_list.clear()
print(f"After clear(): {my_list}")  # OUTPUT: After clear(): []

print("\n" + "=" * 80)  # OUTPUT: (blank line)
print("7. SEARCHING AND COUNTING LIST ELEMENTS")  # OUTPUT: ================================================================================
print("=" * 80)  # OUTPUT: 7. SEARCHING AND COUNTING LIST ELEMENTS

# 7.1 index() - Returns the INDEX of first occurrence
my_list = [10, 20, 30, 40, 50, 30, 20]
print(f"List: {my_list}")  # OUTPUT: ================================================================================
  # OUTPUT: List: [10, 20, 30, 40, 50, 30, 20]

index_of_30 = my_list.index(30)
print(f"Index of first 30: {index_of_30}")  # OUTPUT: Index of first 30: 2

index_of_40 = my_list.index(40)
print(f"Index of 40: {index_of_40}")  # OUTPUT: Index of 40: 3

# Finding index within a range
index_of_30_after_3 = my_list.index(30, 3)
print(f"Index of 30 starting from index 3: {index_of_30_after_3}")  # OUTPUT: Index of 30 starting from index 3: 5

# 7.2 count() - Returns the NUMBER OF OCCURRENCES
count_of_30 = my_list.count(30)
print(f"\nCount of 30 in list: {count_of_30}")  # OUTPUT: (blank line)
  # OUTPUT: Count of 30 in list: 2

count_of_20 = my_list.count(20)
print(f"Count of 20 in list: {count_of_20}")  # OUTPUT: Count of 20 in list: 2

count_of_99 = my_list.count(99)
print(f"Count of 99 (not in list): {count_of_99}")  # OUTPUT: Count of 99 (not in list): 0

# 7.3 Using 'in' operator - Check if item exists
my_list = [10, 20, 30, 40, 50]
print(f"\nList: {my_list}")  # OUTPUT: (blank line)
  # OUTPUT: List: [10, 20, 30, 40, 50]
print(f"20 in my_list: {20 in my_list}")  # OUTPUT: 20 in my_list: True
print(f"99 in my_list: {99 in my_list}")  # OUTPUT: 99 in my_list: False
print(f"10 not in my_list: {10 not in my_list}")  # OUTPUT: 10 not in my_list: False

print("\n" + "=" * 80)  # OUTPUT: (blank line)
print("8. SORTING AND ORDERING LISTS")  # OUTPUT: ================================================================================
print("=" * 80)  # OUTPUT: 8. SORTING AND ORDERING LISTS

# 8.1 sort() - Sorts list IN PLACE in ascending order (modifies original)
my_list = [50, 10, 40, 20, 30]
print(f"Original list: {my_list}")  # OUTPUT: ================================================================================
  # OUTPUT: Original list: [50, 10, 40, 20, 30]
my_list.sort()
print(f"After sort(): {my_list} [Sorted in ascending order]")  # OUTPUT: After sort(): [10, 20, 30, 40, 50] [Sorted in ascending order]

# Sorting in descending order
my_list = [50, 10, 40, 20, 30]
my_list.sort(reverse=True)
print(f"After sort(reverse=True): {my_list}")  # OUTPUT: After sort(reverse=True): [50, 40, 30, 20, 10]

# Sorting with custom key function
my_list = ["apple", "pie", "a", "programming"]
my_list.sort(key=len)
print(f"After sort(key=len): {my_list} [Sorted by string length]")  # OUTPUT: After sort(key=len): ['a', 'pie', 'apple', 'programming'] [Sorted by string length]

# Sorting numbers by absolute value
my_list = [5, -3, 8, -1, 2, -10]
my_list.sort(key=abs)
print(f"After sort(key=abs): {my_list} [Sorted by absolute value]")  # OUTPUT: After sort(key=abs): [-1, 2, -3, 5, 8, -10] [Sorted by absolute value]

# 8.2 sorted() - Returns a NEW sorted list (doesn't modify original)
my_list = [50, 10, 40, 20, 30]
print(f"\nOriginal list: {my_list}")  # OUTPUT: (blank line)
  # OUTPUT: Original list: [50, 10, 40, 20, 30]
sorted_list = sorted(my_list)
print(f"sorted() result: {sorted_list}")  # OUTPUT: sorted() result: [10, 20, 30, 40, 50]
print(f"Original list after sorted(): {my_list} [Unchanged]")  # OUTPUT: Original list after sorted(): [50, 10, 40, 20, 30] [Unchanged]

# 8.3 reverse() - Reverses list IN PLACE (modifies original)
my_list = [1, 2, 3, 4, 5]
print(f"\nOriginal list: {my_list}")  # OUTPUT: (blank line)
  # OUTPUT: Original list: [1, 2, 3, 4, 5]
my_list.reverse()
print(f"After reverse(): {my_list}")  # OUTPUT: After reverse(): [5, 4, 3, 2, 1]

# 8.4 reversed() - Returns a reverse iterator (doesn't modify original)
my_list = [1, 2, 3, 4, 5]
reversed_list = list(reversed(my_list))
print(f"list(reversed()): {reversed_list}")  # OUTPUT: list(reversed()): [5, 4, 3, 2, 1]
print(f"Original list after reversed(): {my_list} [Unchanged]")  # OUTPUT: Original list after reversed(): [1, 2, 3, 4, 5] [Unchanged]

print("\n" + "=" * 80)  # OUTPUT: (blank line)
print("9. COPYING LISTS (SHALLOW vs DEEP COPY)")  # OUTPUT: ================================================================================
print("=" * 80)  # OUTPUT: 9. COPYING LISTS (SHALLOW vs DEEP COPY)

# 9.1 Shallow copy with copy() method
original_list = [1, 2, 3, [4, 5]]
print(f"Original list: {original_list}")  # OUTPUT: ================================================================================
  # OUTPUT: Original list: [1, 2, 3, [4, 5]]

shallow_copy = original_list.copy()
print(f"Shallow copy: {shallow_copy}")  # OUTPUT: Shallow copy: [1, 2, 3, [4, 5]]

# Modifying nested element - affects both!
shallow_copy[3].append(6)
print(f"After shallow_copy[3].append(6):")  # OUTPUT: After shallow_copy[3].append(6):
print(f"  Original list: {original_list} [AFFECTED!]")  # OUTPUT:   Original list: [1, 2, 3, [4, 5, 6]] [AFFECTED!]
print(f"  Shallow copy: {shallow_copy}")  # OUTPUT:   Shallow copy: [1, 2, 3, [4, 5, 6]]

# 9.2 Shallow copy with slicing
original_list = [1, 2, 3, [4, 5]]
shallow_copy2 = original_list[:]
print(f"\nOriginal list: {original_list}")  # OUTPUT: (blank line)
  # OUTPUT: Original list: [1, 2, 3, [4, 5]]
print(f"Shallow copy using slicing: {shallow_copy2}")  # OUTPUT: Shallow copy using slicing: [1, 2, 3, [4, 5]]

# 9.3 Assignment creates reference (NOT a copy)
original_list = [1, 2, 3]
reference_list = original_list
reference_list.append(4)
print(f"\nAfter reference_list.append(4):")  # OUTPUT: (blank line)
  # OUTPUT: After reference_list.append(4):
print(f"  Original list: {original_list} [AFFECTED!]")  # OUTPUT:   Original list: [1, 2, 3, 4] [AFFECTED!]
print(f"  Reference list: {reference_list}")  # OUTPUT:   Reference list: [1, 2, 3, 4]

# 9.4 Deep copy using copy module
import copy
original_list = [1, 2, 3, [4, 5]]
deep_copy = copy.deepcopy(original_list)
deep_copy[3].append(6)
print(f"\nAfter deep_copy[3].append(6):")  # OUTPUT: (blank line)
  # OUTPUT: After deep_copy[3].append(6):
print(f"  Original list: {original_list} [NOT affected!]")  # OUTPUT:   Original list: [1, 2, 3, [4, 5]] [NOT affected!]
print(f"  Deep copy: {deep_copy}")  # OUTPUT:   Deep copy: [1, 2, 3, [4, 5, 6]]

print("\n" + "=" * 80)  # OUTPUT: (blank line)
print("10. JOINING AND COMBINING LISTS")  # OUTPUT: ================================================================================
print("=" * 80)  # OUTPUT: 10. JOINING AND COMBINING LISTS

# 10.1 Using + operator - Creates NEW list
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(f"List1: {list1}, List2: {list2}")  # OUTPUT: ================================================================================
  # OUTPUT: List1: [1, 2, 3], List2: [4, 5, 6]

joined_list = list1 + list2
print(f"list1 + list2: {joined_list}")  # OUTPUT: list1 + list2: [1, 2, 3, 4, 5, 6]
print(f"Original lists unchanged: list1={list1}, list2={list2}")  # OUTPUT: Original lists unchanged: list1=[1, 2, 3], list2=[4, 5, 6]

# 10.2 Using extend() - Modifies original list
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(f"\nAfter list1.extend(list2): {list1}")  # OUTPUT: (blank line)
  # OUTPUT: After list1.extend(list2): [1, 2, 3, 4, 5, 6]

# 10.3 Using * operator - Repeats list elements
list1 = [1, 2, 3]
repeated_list = list1 * 3
print(f"\n[1, 2, 3] * 3: {repeated_list}")  # OUTPUT: (blank line)
  # OUTPUT: [1, 2, 3] * 3: [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 10.4 Using append() - Adds entire object (nesting)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.append(list2)
print(f"\nAfter list1.append(list2): {list1} [list2 added as nested list]")  # OUTPUT: (blank line)
  # OUTPUT: After list1.append(list2): [1, 2, 3, [4, 5, 6]] [list2 added as nested list]

# 10.5 Using unpacking
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = [*list1, *list2]
print(f"\nUsing unpacking [*list1, *list2]: {combined}")  # OUTPUT: (blank line)
  # OUTPUT: Using unpacking [*list1, *list2]: [1, 2, 3, 4, 5, 6]

print("\n" + "=" * 80)  # OUTPUT: (blank line)
print("11. LIST COMPREHENSIONS (ADVANCED & PYTHONIC)")  # OUTPUT: ================================================================================
print("=" * 80)  # OUTPUT: 11. LIST COMPREHENSIONS (ADVANCED & PYTHONIC)

# 11.1 Basic list comprehension
squares = [x**2 for x in range(1, 6)]
print(f"Squares (1-5): {squares}")  # OUTPUT: ================================================================================
  # OUTPUT: Squares (1-5): [1, 4, 9, 16, 25]

# 11.2 List comprehension with condition
evens = [x for x in range(1, 11) if x % 2 == 0]
print(f"Even numbers (1-10): {evens}")  # OUTPUT: Even numbers (1-10): [2, 4, 6, 8, 10]

# 11.3 List comprehension with if-else
numbers = [x if x % 2 == 0 else -x for x in range(1, 6)]
print(f"Even positive, odd negative: {numbers}")  # OUTPUT: Even positive, odd negative: [-1, 2, -3, 4, -5]

# 11.4 Nested list comprehension
matrix = [[x*y for x in range(1, 4)] for y in range(1, 4)]
print(f"3x3 multiplication table:\n{matrix}")  # OUTPUT: 3x3 multiplication table:
  # OUTPUT: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# 11.5 Flattening nested lists
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for sublist in nested for item in sublist]
print(f"Flattened nested list: {flattened}")  # OUTPUT: Flattened nested list: [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("\n" + "=" * 80)  # OUTPUT: (blank line)
print("12. ADVANCED LIST OPERATIONS")  # OUTPUT: ================================================================================
print("=" * 80)  # OUTPUT: 12. ADVANCED LIST OPERATIONS

# 12.1 map() - Apply function to all elements
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"Using map() to square: {squared}")  # OUTPUT: ================================================================================
  # OUTPUT: Using map() to square: [1, 4, 9, 16, 25]

# 12.2 filter() - Filter elements based on condition
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Using filter() for evens: {evens}")  # OUTPUT: Using filter() for evens: [2, 4, 6, 8, 10]

# 12.3 sum() - Calculate sum of elements
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(f"Sum of {numbers}: {total}")  # OUTPUT: Sum of [1, 2, 3, 4, 5]: 15

# 12.4 min() and max() - Find minimum and maximum
numbers = [10, 5, 20, 3, 15]
print(f"List: {numbers}")  # OUTPUT: List: [10, 5, 20, 3, 15]
print(f"min(): {min(numbers)}, max(): {max(numbers)}")  # OUTPUT: min(): 3, max(): 20

# 12.5 any() and all() - Boolean operations
numbers = [2, 4, 6, 8, 10]
print(f"List: {numbers}")  # OUTPUT: List: [2, 4, 6, 8, 10]
print(f"any(x % 3 == 0 for x in list): {any(x % 3 == 0 for x in numbers)}")  # OUTPUT: any(x % 3 == 0 for x in list): True
print(f"all(x % 2 == 0 for x in list): {all(x % 2 == 0 for x in numbers)}")  # OUTPUT: all(x % 2 == 0 for x in list): True

# 12.6 zip() - Combine multiple lists
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = list(zip(list1, list2))
print(f"zip([1,2,3], ['a','b','c']): {zipped}")  # OUTPUT: zip([1,2,3], ['a','b','c']): [(1, 'a'), (2, 'b'), (3, 'c')]

# 12.7 enumerate() - Get index and value
my_list = ['a', 'b', 'c', 'd']
for index, value in enumerate(my_list):  # OUTPUT: (loop outputs below)
    print(f"  Index {index}: {value}")  # OUTPUT: Index 0: a, Index 1: b, Index 2: c, Index 3: d

print("\n" + "=" * 80)  # OUTPUT: (blank line)
print("13. ITERATING THROUGH LISTS")  # OUTPUT: ================================================================================
print("=" * 80)  # OUTPUT: 13. ITERATING THROUGH LISTS

my_list = [10, 20, 30, 40, 50]

# 13.1 Simple for loop
print("Using for loop:")  # OUTPUT: Using for loop:
for item in my_list:  # OUTPUT: (loop outputs below)
    print(f"  {item}")  # OUTPUT: 10, 20, 30, 40, 50

# 13.2 For loop with index
print("\nUsing for loop with index:")  # OUTPUT: (blank line)
  # OUTPUT: Using for loop with index:
for i in range(len(my_list)):  # OUTPUT: (loop outputs below)
    print(f"  Index {i}: {my_list[i]}")  # OUTPUT: Index 0: 10, Index 1: 20, Index 2: 30, Index 3: 40, Index 4: 50

# 13.3 For loop with enumerate
print("\nUsing enumerate():")  # OUTPUT: (blank line)
  # OUTPUT: Using enumerate():
for index, value in enumerate(my_list):  # OUTPUT: (loop outputs below)
    print(f"  {index}: {value}")  # OUTPUT: 0: 10, 1: 20, 2: 30, 3: 40, 4: 50

# 13.4 For loop with reversed
print("\nUsing reversed():")  # OUTPUT: (blank line)
  # OUTPUT: Using reversed():
for item in reversed(my_list):  # OUTPUT: (loop outputs below)
    print(f"  {item}")  # OUTPUT: 50, 40, 30, 20, 10

# 13.5 List comprehension iteration
print("\nList comprehension iteration:")  # OUTPUT: (blank line)
  # OUTPUT: List comprehension iteration:
squares = [x**2 for x in my_list]
print(f"  {squares}")  # OUTPUT:   [100, 400, 900, 1600, 2500]

print("\n" + "=" * 80)  # OUTPUT: (blank line)
print("14. NESTED LISTS (LISTS OF LISTS)")  # OUTPUT: ================================================================================
print("=" * 80)  # OUTPUT: 14. NESTED LISTS (LISTS OF LISTS)

# 14.1 Creating nested lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"2D Matrix: {matrix}")  # OUTPUT: ================================================================================
  # OUTPUT: 2D Matrix: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 14.2 Accessing nested elements
print(f"Element at [0][0]: {matrix[0][0]}")  # OUTPUT: Element at [0][0]: 1
print(f"Element at [1][2]: {matrix[1][2]}")  # OUTPUT: Element at [1][2]: 6
print(f"Element at [2][1]: {matrix[2][1]}")  # OUTPUT: Element at [2][1]: 8

# 14.3 Modifying nested elements
matrix[1][1] = 50
print(f"After matrix[1][1] = 50: {matrix}")  # OUTPUT: After matrix[1][1] = 50: [[1, 2, 3], [4, 50, 6], [7, 8, 9]]

# 14.4 Iterating through nested lists
print("\nIterating through matrix:")  # OUTPUT: (blank line)
  # OUTPUT: Iterating through matrix:
for row in matrix:  # OUTPUT: (loop outputs below)
    for element in row:  # OUTPUT: 1 2 3 4 50 6 7 8 9
        print(f"  {element}")

# 14.5 Flattening nested lists
flat_list = [item for row in matrix for item in row]
print(f"Flattened: {flat_list}")  # OUTPUT: Flattened: [1, 2, 3, 4, 50, 6, 7, 8, 9]

print("\n" + "=" * 80)
print("15. LIST METHODS REFERENCE (COMPLETE SUMMARY)")
print("=" * 80)
print("""
METHOD              | DESCRIPTION                              | EXAMPLE
--------------------|------------------------------------------|----------
append(item)        | Add item to end                         | list.append(5)
insert(i, item)     | Insert item at index i                  | list.insert(0, 'a')
extend(iterable)    | Add all items from iterable             | list.extend([1,2,3])
remove(item)        | Remove first occurrence of item         | list.remove(5)
pop([i])            | Remove and return item at index i       | list.pop(0)
clear()             | Remove all items                        | list.clear()
index(item, [,s,e]) | Return index of first occurrence        | list.index(5)
count(item)         | Return count of occurrences             | list.count(5)
sort([key,reverse]) | Sort list in place                      | list.sort()
reverse()           | Reverse list in place                   | list.reverse()
copy()              | Return shallow copy of list             | copy = list.copy()
""")

print("\n" + "=" * 80)
print("16. PERFORMANCE CONSIDERATIONS")
print("=" * 80)
print("""
OPERATION                  | TIME COMPLEXITY | NOTES
---------------------------|-----------------|----------------------------------
Accessing element [i]      | O(1)            | Direct access via index
Appending to end           | O(1) amortized  | Usually fast, except when resizing
Inserting at beginning     | O(n)            | All elements must shift
Removing from end          | O(1)            | Fast operation
Removing from beginning    | O(n)            | All elements must shift
Searching (index/count)    | O(n)            | Linear search required
Sorting                    | O(n log n)      | Using Timsort algorithm
Copying                    | O(n)            | Must copy all elements
Slicing                    | O(k)            | Where k is slice length
""")

print("\n" + "=" * 80)  # OUTPUT: (blank line)
print("17. COMMON PITFALLS AND BEST PRACTICES")  # OUTPUT: ================================================================================
print("=" * 80)  # OUTPUT: 17. COMMON PITFALLS AND BEST PRACTICES

# Pitfall 1: Modifying while iterating
print("PITFALL 1: Modifying list while iterating")  # OUTPUT: PITFALL 1: Modifying list while iterating
my_list = [1, 2, 3, 4, 5]
# Don't do this!
# for item in my_list:
#     if item == 3:
#         my_list.remove(item)  # Dangerous!

# Better approach
my_list = [1, 2, 3, 4, 5]
my_list = [x for x in my_list if x != 3]
print(f"  Using comprehension: {my_list}")  # OUTPUT:   Using comprehension: [1, 2, 4, 5]

# Pitfall 2: Shared references in list of lists
print("\nPITFALL 2: Shared references")  # OUTPUT: (blank line)
  # OUTPUT: PITFALL 2: Shared references
wrong_way = [[0] * 3 for _ in range(3)]
wrong_way[0][0] = 5
print(f"  Correct way - modifying one element: {wrong_way}")  # OUTPUT:   Correct way - modifying one element: [[5, 0, 0], [0, 0, 0], [0, 0, 0]]

# Pitfall 3: Assuming += modifies vs creates new list
print("\nPITFALL 3: += behavior")  # OUTPUT: (blank line)
  # OUTPUT: PITFALL 3: += behavior
list1 = [1, 2, 3]
original_id = id(list1)
list1 += [4, 5]
print(f"  += on list modifies in place (same id): {id(list1) == original_id}")  # OUTPUT:   += on list modifies in place (same id): True

my_tuple = (1, 2, 3)
original_id = id(my_tuple)
my_tuple += (4, 5)
print(f"  += on tuple creates new object (different id): {id(my_tuple) != original_id}")  # OUTPUT:   += on tuple creates new object (different id): True

print("\n" + "=" * 80)  # OUTPUT: (blank line)
print("18. PRACTICAL EXAMPLES AND USE CASES")  # OUTPUT: ================================================================================
print("=" * 80)  # OUTPUT: 18. PRACTICAL EXAMPLES AND USE CASES

# Example 1: Counting word frequency
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_counts = {}
for word in words:
    word_counts[word] = words.count(word)
print(f"Word frequency: {word_counts}")  # OUTPUT: Word frequency: {'apple': 3, 'banana': 2, 'cherry': 1}

# Example 2: Removing duplicates while preserving order
numbers = [1, 2, 3, 2, 4, 1, 5, 3]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print(f"Remove duplicates (preserving order): {unique_numbers}")  # OUTPUT: Remove duplicates (preserving order): [1, 2, 3, 4, 5]

# Example 3: Finding common elements in two lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common = [x for x in list1 if x in list2]
print(f"Common elements: {common}")  # OUTPUT: Common elements: [3, 4, 5]

# Example 4: Transpose a matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(f"Original matrix: {matrix}")  # OUTPUT: Original matrix: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Transposed: {transposed}")  # OUTPUT: Transposed: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# Example 5: Finding missing numbers in sequence
numbers = [1, 2, 3, 5, 6, 8, 9, 10]
full_range = set(range(min(numbers), max(numbers) + 1))
missing = sorted(list(full_range - set(numbers)))
print(f"Missing numbers: {missing}")  # OUTPUT: Missing numbers: [4, 7]

print("\n" + "=" * 80)
print("19. SUMMARY AND KEY TAKEAWAYS")
print("=" * 80)
print("""
✓ Lists are ordered, mutable, and can contain mixed data types
✓ Use indexing (0-based) and slicing to access elements
✓ append() adds to end, insert() adds at specific position
✓ remove() deletes by value, pop() deletes by index
✓ sort() and reverse() modify in place
✓ List comprehensions are the Pythonic way to create lists
✓ Use copy.deepcopy() for nested lists to avoid reference issues
✓ Be careful when modifying lists during iteration
✓ Understand time complexity for performance-critical code
✓ Lists are versatile for stacks, queues, and general data storage
""")

print("\n" + "=" * 80)
print("END OF COMPREHENSIVE LISTS TUTORIAL")
print("=" * 80)
#In summary, there are several ways to join lists in Python, including using the + operator, the extend() method, the * operator, and the append() method. Each method has its own use case and can be used depending on your specific needs when working with lists.
#List Comprehensions
#List comprehensions are a concise way to create lists in Python. They provide a more readable and efficient way to generate lists compared to using traditional for loops. The syntax for a list comprehension is as follows:
#new_list = [expression for item in iterable if condition]
#Here, expression is the value that will be added to the new list for each item in the iterable that satisfies the condition. The condition is optional, and if it is not provided, all items in the iterable will be included in the new list.
#Here are some examples of using list comprehensions in Python:
#Creating a list of squares using a list comprehension
squares = [x**2 for x in range(10)]
print(squares)  # OUTPUT: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#Creating a list of even numbers using a list comprehension with a condition
even_numbers = [x for x in range(20) if x % 2 == 0]
print(even_numbers)  # OUTPUT: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
#Creating a list of the first letters of each word in a list of words
words = ["Hello", "World", "Python", "Programming"]
first_letters = [word[0] for word in words]
print(first_letters)  # OUTPUT: ['H', 'W', 'P', 'P']
#Creating a list of tuples containing the number and its square
number_square_tuples = [(x, x**2) for x in range(5)]
print(number_square_tuples)  # OUTPUT: [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)]
#flattening a list of lists using a list comprehension
list_of_lists = [[1, 2], [3, 4], [5, 6]]
flattened_list = [item for sublist in list_of_lists for item in sublist]
print(flattened_list)  # OUTPUT: [1, 2, 3, 4, 5, 6]
#In summary, list comprehensions are a powerful and efficient way to create lists in Python. They allow you to generate lists in a more concise and readable manner compared to traditional for loops. By using list comprehensions, you can easily create new lists based on existing iterables while applying conditions and transformations to the items in the iterable.
#List Iteration
#You can iterate over the items in a list using a for loop. This allows you to perform operations on each item in the list. Here are some examples of how to iterate over a list in Python:
#Iterating over a list of numbers
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)  # OUTPUT: 1, 2, 3, 4, 5
# Output:
# 1
# 2
# 3
# 4
# 5
#Iterating over a list of strings
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # OUTPUT: apple, banana, cherry
# Output:
# apple
# banana
# cherry
#Iterating over a list of lists
list_of_lists = [[1, 2], [3, 4], [5, 6]]
for sublist in list_of_lists:
    for item in sublist:
        print(item)  # OUTPUT: 1, 2, 3, 4, 5, 6
# Output:
# 1
# 2         
# 3
# 4
# 5
# 6
#Using enumerate() to get the index and value while iterating over a list
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")  # OUTPUT: Index: 0, Fruit: apple | Index: 1, Fruit: banana | Index: 2, Fruit: cherry
# Output:
# Index: 0, Fruit: apple
# Index: 1, Fruit: banana
# Index: 2, Fruit: cherry
#Using zip() to iterate over two lists simultaneously
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for num, letter in zip(list1, list2):
    print(f"Number: {num}, Letter: {letter}")  # OUTPUT: Number: 1, Letter: a | Number: 2, Letter: b | Number: 3, Letter: c
# Output:
# Number: 1, Letter: a
# Number: 2, Letter: b
# Number: 3, Letter: c
#In summary, iterating over a list in Python is a common operation that allows you to perform actions on each item in the list. You can use a simple for loop to iterate over the items, or you can use functions like enumerate() and zip() to get additional information while iterating. Understanding how to iterate over lists is essential for working with data in Python and performing various operations on the items in a list.