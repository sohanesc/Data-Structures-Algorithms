"""
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
"""

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
for i in range(n, 0, -1):
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()

print("Static Version\nOR\nDynamic Version\n")

for i in range(1, n // 2 + 1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
for i in range(n // 2, 0, -1):
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()
