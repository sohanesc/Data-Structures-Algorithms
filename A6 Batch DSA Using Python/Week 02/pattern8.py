"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

for i in range(n, 0, -1):
    for j in range(1, i):
        print(j, end=" ")
    print()

print("Static Version\nOR\nDynamic Version\n")

for i in range(1, n // 2 + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

for i in range(n // 2, 0, -1):
    for j in range(1, i):
        print(j, end=" ")
    print()
