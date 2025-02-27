"""
Q2. Ask a number from user. Print all the factors of a that number. (Order 
does not matter, just print it)
 Example 1:
 Enter a number = 20
 Output:
 1 2 4 5 10 20
 Example 2:
 Enter a number = 100
 Output:
 1 2 4 5 10 20 25 50 100
 """

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
