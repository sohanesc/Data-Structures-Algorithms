"""
List comprehension provides a concise way to create lists using a single line of code.

new_list = [`expression` for `item` in `iterable` if `condition`]
"""

squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# With a condition ↙️

even_numbers = [x for x in range(20) if x % 2 == 0]
print(even_numbers)  # Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
