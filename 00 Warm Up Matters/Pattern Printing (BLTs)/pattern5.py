n = int(input("Enter the number of rows: "))

# Loop for each row
for i in range(n):
    # Loop to print i in each column
    for j in range(n-i):
        print("*", end=" ")
    # Print a new line after each row
    print()