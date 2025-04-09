"""
Rules:

1. Should start with a-z A-Z
2. Can contain a-z A-Z _ 0-9
3. Can't contain symbols $^#$%&*+-
4. Can't have reserve keywords (print, for, in, break)
"""

a = 32
print(type(a), id(a))
a = "something"
print(type(a), id(a))


b = 32
print(type(b), id(b))
b = 33
print(type(b), id(b))
b = "something"
print(type(b), id(b))


"""
We get here, Same value has shared same memory location

Python uses a mechanism called interning for certain immutable objects (like integers and strings) to save memory. This means that variables with the same value may share the same memory location under specific circumstances. Here's an example:
a = 42
b = 42

print(id(a))  # Memory location of a
print(id(b))  # Memory location of b

In this example, a and b have the same value (42), so they share the same memory location.



However, this behavior doesn't always apply to mutable objects (e.g., lists, dictionaries) or larger numbers and strings created dynamically. If you test with a more complex data type or unique object, they'll have distinct memory locations.
"""
