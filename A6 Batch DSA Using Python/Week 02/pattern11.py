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
    for j in range(1, n - i + 1):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print(k, end=" ")
    print()
for i in range(n - 1, 0, -1):
    for j in range(1, n - i + 1):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print(k, end=" ")
    print()

print("\nOR this one for second part ↙️")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(" ", end=" ")
    for k in range(1, n - i + 1):
        print(k, end=" ")
    print()


print("\nOR\n")

for i in range(n, 0, -1):
    for j in range(1, i):
        print(" ", end=" ")
    for k in range(1, n - i + 2):
        print(k, end=" ")
    print()
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(" ", end=" ")
    for k in range(1, n - i + 1):
        print(k, end=" ")
    print()
