"""
+ve -> positive
-ve -> negetive
0 -> zero
"""

num = int(input("Enter a number = "))

if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive")
else:
    print("Negetive")
