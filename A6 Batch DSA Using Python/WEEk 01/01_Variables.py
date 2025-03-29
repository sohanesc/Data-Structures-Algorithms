"""
Rules:

1. Should start with a-z A-Z
2. Can contain a-z A-Z _ 0-9
3. Can't contain symbols $^#$%&*+-
4. Can't have reserve keywords (print, for, in, break)
"""

a = 10
b = 20
c = a + b + a + b
c = c * c - c
print(c)

_ = 33
__ = 33
print(_ + __)


name = "sohan"
age = 1000
print("detail: ", name, age, "age")
print(f"detail: {name} {type(name), name, age}")
