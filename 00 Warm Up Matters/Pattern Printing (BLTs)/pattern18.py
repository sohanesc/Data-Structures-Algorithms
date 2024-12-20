n = int(input("Enter the number of rows: "))

# Loop for rows
for i in range(n):
    for j in range(i, -1, -1):
        print(chr(65 + n - 1 - j), end=" ")
    print()
