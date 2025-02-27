"""
Q1. Factorial of a Number: Write a program to calculate the factorial of a 
given number using a loop.
 Example:
 Enter a number = 5
 Output:
 120
 Explanation:
 Factorial of 5 is 5 x 4 x 3 x 2 x 1
 """

n = int(input("Enter a number: "))

factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(factorial)