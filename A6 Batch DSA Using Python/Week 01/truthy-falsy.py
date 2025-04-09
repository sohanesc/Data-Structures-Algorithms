"""
DT -> bool

Truthy
int -> 1, 8, 9, -10, -1, 55
float -> 0.0001, 1.555, 2.55, -9.66666
str -> " ", "abc, "a", "$"

Falsy
int -> 0
float -> 0.0
str -> ""
None
"""

a = bool(1.5)
print(a)

b = bool(0)
print(b)

c = bool(None)
print(c)
