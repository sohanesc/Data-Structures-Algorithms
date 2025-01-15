n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    # Print the increasing part
    for j in range(1, i + 1):
        print(j, end="")
    
    # Print the spaces in the middle
    for j in range(2 * (n - i)):
        print(" ", end="")
    
    # Print the decreasing part
    for j in range(i, 0, -1):
        print(j, end="")
    
    print()
