n = int(input("Enter the number of rows: "))

# Loop for upper half
for i in range(n):
    for j in range(n - i):
        print("*", end="")
    for j in range(2 * i):
        print(" ", end="")
    for j in range(n - i):
        print("*", end="")
    print()

# Loop for lower half
for i in range(n - 1):
    for j in range(i + 2):
        print("*", end="")
    for j in range(2 * (n - i - 2)):
        print(" ", end="")
    for j in range(i + 2):
        print("*", end="")
    print()
