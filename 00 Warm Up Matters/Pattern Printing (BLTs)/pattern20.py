n = int(input("Enter the number of rows: "))

# Top half
for i in range(n - 1):
    for j in range(i + 1):
        print("*", end="")
    for j in range(2 * (n - i - 1)):
        print(" ", end="")
    for j in range(i + 1):
        print("*", end="")
    print()

# Bottom half
for i in range(n - 1, -1, -1):
    for j in range(i + 1):
        print("*", end="")
    for j in range(2 * (n - i - 1)):
        print(" ", end="")
    for j in range(i + 1):
        print("*", end="")
    print()
