n = int(input("Enter the number of rows: "))

# Loop for rows
for i in range(n):
    # Print leading spaces
    for j in range(n - i - 1):
        print(" ", end="")
    
    # Print increasing part
    for j in range(i + 1):
        print(chr(65 + j), end="")
    
    # Print decreasing part
    for j in range(i - 1, -1, -1):
        print(chr(65 + j), end="")
    
    print()
