n = int(input("Enter the number of rows: "))

# Loop for row
for i in range(n, 0, -1):
    # Loop for column
    for j in range(1, i+1):
        print(j, end=" ")
    # Print a new line after each row
    print()