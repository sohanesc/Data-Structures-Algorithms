"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *

TC -> O(n^2)
"""

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print("*", end="  ")
    print()
