n = int(input("Enter the number of rows: "))

# Loop for rows
for i in range(n):
    # Loop for columns
    for j in range(n - i):
        print(chr(65 + j), end=" ")
    print()
