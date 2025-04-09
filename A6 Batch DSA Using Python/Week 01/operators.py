"""
Types of operators

1. Arithmetic   (+, -, *, /, **, //, %)
2. Assignment   (=, +=, -=, *=, /=, //=, %=)
3. Comparison   (==, !=, >, <, >=, <=)
4. Logical      (and, or, not)
5. Membership   (in, not in)
6. Identity     (is, is not)
7. Bitwise      (&, |, ^, ~, <<, >>)
"""

a = 10
b = 3

# Arithmetic operators
print("##### Arithmetic operators #####")
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a**b)  # power
print(a // b)  # floor division (always in integer)
print(a % b)  # modulus


# Assignment operators
print("##### Assignment operators #####")
a = 5
b = 5
print(f"a = {a}")
print(f"id(a) = {id(a)}")
print(f"b = {b}")
print(f"id(b) = {id(b)}")


b = 10
print(f"b = {b}")
print(f"id(b) = {id(b)}")

a = 100
print(f"a = {a}")
print(f"id(a) = {id(a)}")
# a = a + 3
# print(a)
# print(id(a))


# Logical operators
"""
Logical Operators (to compare 2 or more comparisions)
AND
C1  C2  Result
F   F   F
F   T   F
T   F   F
T   T   T


OR
C1  C2  Result
F   F   F
F   T   T
T   F   T
T   T   T

NOT (reverse the result)
"""

physics = 33
chemistry = 99

# print(physics > 33 and chemistry > 33)
# print(physics > 33 or chemistry > 33)

# print(not (physics > 33 and chemistry > 33))
# print(not physics > 33 and chemistry > 33)
print(not (not physics > 33 and not chemistry > 33))
