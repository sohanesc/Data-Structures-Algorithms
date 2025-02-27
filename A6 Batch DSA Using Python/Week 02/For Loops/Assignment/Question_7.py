"""
Q7. Write a program to repeatedly sum the digits of a number until only a 
single-digit number is obtained. The process involves summing the digits 
of the number and then repeating the process with the result until the 
number is reduced to a single digit.
 Requirements:
 1. You are given a positive integer n (Ask n from user)
 2. You need to find the sum of the digits of n, and if the result is greater 
than 9, repeat the process.
 3. Continue summing the digits until the result is a single-digit number.
 4. Do not use lists, strings, dictionaries, or nested loops.
 Example Scenarios to Consider:
 1. Input: 9875
 Output: 2
 Explanation:
 Step 1: 9 + 8 + 7 + 5 = 29
 Step 2: 2 + 9 = 11
 Step 3: 1 + 1 = 2 (single digit obtained).
2. Input: 12345
 Output: 6
 Explanation:
 Step 1: 1 + 2 + 3 + 4 + 5 = 15
 Step 2: 1 + 5 = 6 (single digit obtained).
 3. Input: 99
 Output: 9
 Explanation:
 Step 1: 9 + 9 = 18
 Step 2: 1 + 8 = 9 (single digit obtained).
 4. Input: 0
 Output: 0
 Explanation: The sum of the digits of 0 is 0, which is already a single 
digit.
"""

n = int(input("Enter a number = "))

sum_of_digits = 0

while n > 9:
    for i in str(n):
        sum_of_digits += int(i)
    n = sum_of_digits
    sum_of_digits = 0

print(n)