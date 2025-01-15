n = int(input("Enter the number of rows: "))

# Loop for rows
for i in range(n):
    for j in range(i + 1):
        # Print 1 if the sum of row and column indexes is even, otherwise print 0
        if (i + j) % 2 == 0:
            print("1 ", end="")
        else:
            print("0 ", end="")
    print()
