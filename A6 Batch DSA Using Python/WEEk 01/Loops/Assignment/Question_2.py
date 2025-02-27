"""
 Q2. Ask a positive number from user. Calculate the total sum of all the 
numbers from 1 to n. 
Example 1:
 Enter a number = 6
 Output:
 21
 Example 2:
 Enter a number = 10
 Output:
 55
 """

n = int(input("Enter a positive number: "))

sum = 0
i = 1

while i <= n:
    sum += i
    i += 1

print(sum)