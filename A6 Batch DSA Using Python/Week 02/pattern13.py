"""
1 2 1 2 1
1 2 1 2
1 2 1
1 2
1
"""

n = int(input("Enter a number: "))

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        if j % 2 == 1:
            print("1", end=" ")
        else:
            print("2", end=" ")
    print()
