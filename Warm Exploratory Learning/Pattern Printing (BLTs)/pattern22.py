def print_pattern(n):
    # Adjusting the pattern to follow the desired format
    k = n // 2 + 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(k - min(i-1, j-1, n-i, n-j), end=" ")
        print()

# Set the size of the pattern
n = int(input("Enter the size of the grid: "))
print_pattern(n)

