"""
Types of Data:
Integer(int) - 5, 8, 0, -3, -1000
Float (float) - 5. 5, 3.14, 5.6793
Complex Numbers
String (str) - "Sohan", "Code & Math", "a", 'Someone'
Booleans (bool) - True, False
List
Tuple
Set
Dictionary
NoneType -> None
"""

"""
Type Casting / Type Conversion
From one data type to another

int -> float
float -> int
str -> int
float -> str
bool -> int
int -> bool
"""

a = int("1000")
# a = int("1000.2")  # This will throw an error
b = int("2000")
print(type(a + b), (a + b))
c = float(a + b)
print(type(c), c)

d = int(-5.98)  # -5 nearest to 0
e = int(5.98)  # 5 nearest to 0
print(d, e)
