"""
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
TC ->  O(n(n+1)/2) or O(n^2)
"""

n = int(input("Enter a number: "))

for i in range(1, n + 1):  # default incrementing by 1
    for j in range(1, i + 1):
        print(n - j + 1, end=" ")  # n - j + 1
    print()

print("\nOR\n")

for i in range(n, 0, -1):  # decrementing by -1
    for j in range(n, i - 1, -1):  # decrementing by -1
        print(j, end=" ")  # j
    print()
