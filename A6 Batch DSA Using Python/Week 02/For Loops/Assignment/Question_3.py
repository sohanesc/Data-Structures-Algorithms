"""
Q3. Ask a number from user. Count the number of factors of that number.
 Example 1:
 Enter a number = 20
Output:
 6
 Example 2:
 Enter a number = 100
 Output:
 9
 """

n = int(input("Enter a number: "))

count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

print(count)