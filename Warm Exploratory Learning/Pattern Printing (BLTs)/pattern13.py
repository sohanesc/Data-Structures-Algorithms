n = int(input("Enter the number of rows: "))

# Initial number
num = 1

# Loop for rows
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
