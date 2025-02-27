"""
Q6. Write a program to check if a given number is a perfect number. A 
number is called perfect if it is equal to the sum of its proper divisors 
(divisors excluding the number itself).
 Requirements:
 1. You are given a positive integer n (Ask from user)
 2. Your task is to check if n is a perfect number or not using a loop.
 Example Scenarios to Consider:
1. Input: 6
 Output: True
 Explanation: The divisors of 6 are 1, 2, 3. The sum is 1 + 2 + 3 = 6, so it is 
a perfect number.
 2. Input: 12
 Output: False
 Explanation: The divisors of 12 are 1, 2, 3, 4, 6. The sum is 1 + 2 + 3 + 4 + 6 
= 16, which is not equal to 12.
 3. Input: 28
 Output: True
 Explanation: The divisors of 28 are 1, 2, 4, 7, 14. The sum is 1 + 2 + 4 + 7 + 
14 = 28, so it is a perfect number.
 4. Input: 1
 Output: False
 Explanation: The number 1 has no divisors other than itself, so it is not 
a perfect number.
"""

n = int(input("Enter a number = "))

sum_of_divisors = 0

for i in range(1, n):
    if n % i == 0:
        sum_of_divisors += i
if sum_of_divisors == n:
    print(True)
else:
    print(False)
