"""
Python provides several built-in methods to manipulate lists efficiently. Here are some commonly used ones:

- `append()`: Adds an element at the end of the list.
- `clear()`: Removes all elements from the list.
- `copy()`: Returns a shallow copy of the list.
- `count()`: Returns the number of occurrences of a specified value.
- `extend()`: Adds elements of another iterable to the end of the list.
- `index()`: Returns the index of the first occurrence of a specified value.
- `insert()`: Inserts an element at a specified position.
- `pop()`: Removes and returns the element at a specified position.
- `remove()`: Removes the first occurrence of a specified value.
- `reverse()`: Reverses the order of elements in the list.
- `sort()`: Sorts the list in ascending order by default.

"""

fruits = ["apple", "banana", "cherry", "apple"]

fruits.append("orange")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'apple', 'orange']

print(fruits.count("apple"))  # Output: 2

print(fruits.index("banana"))  # Output: 1

fruits.insert(2, "grape")
print(fruits)  # Output: ['apple', 'banana', 'grape', 'cherry', 'apple', 'orange']

removed_item = fruits.pop(3)
print(removed_item)  # Output: 'cherry'
print(fruits)  # Output: ['apple', 'banana', 'grape', 'apple', 'orange']

fruits.remove("apple")
print(fruits)  # Output: ['banana', 'grape', 'apple', 'orange']

fruits.reverse()
print(fruits)  # Output: ['orange', 'apple', 'grape', 'banana']

fruits.sort()
print(fruits)  # Output: ['apple', 'banana', 'grape', 'orange']
