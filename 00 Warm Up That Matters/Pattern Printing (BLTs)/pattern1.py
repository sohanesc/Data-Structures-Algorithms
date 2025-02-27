n = int(input("Enter the number of rows: "))

# Loop for each row
for i in range(n):
    # Loop to print ❤️ in each column
    for j in range(n):
        print("1", end=" ")
    # Print a new line after each row
    print()

# TC: O(n^2)
