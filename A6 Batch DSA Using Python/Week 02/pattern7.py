"""
1 1 1 1 1
2 2 2 2
3 3 3
4 4
5
TC -> O(n(n+1)/2) or O(n^2)
"""

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    for j in range(1, n - i + 2):
        print(i, end=" ")
    print()

print("\nOR\n")

for i in range(n, 0, -1):
    # print(i, end=" ")
    for j in range(1, i + 1):  # always for 'how many times'
        print(n - i + 1, end=" ")  # it decides 'what to print' in each iteration
    print()
