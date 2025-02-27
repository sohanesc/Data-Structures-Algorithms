"""
Q4. Ask a number from user. Print the sum of all the factors of that number.
 Example 1:
 Enter a number = 20
 Output:
 42
 Example 2:
 Enter a number = 100
 Output:
 217
 """

n = int(input("Enter a number: "))

sum = 0

for i in range(1, n + 1):
    if n % i == 0:
        sum += i

print(sum)
