"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
TC -> O(n(n+1)/2) or O(n^2)
"""

n = int(input("Enter a number: "))


for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
