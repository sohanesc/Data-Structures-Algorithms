"""
	Assignment-19: Simple problems on recursion
1.	Write a recursive function to calculate sum of first N natural numbers.
2.	Write a recursive function to calculate sum of first N odd natural numbers
3.	Write a recursive function to calculate sum of first N even natural numbers
4.	Write a recursive function to calculate factorial of a number.
5.	Write a recursive function to calculate sum of squares of first N natural numbers.
"""

def sumN(n):
    if n == 1:
        return 1
    return n + sumN(n - 1) 

def sumNodd(n):
    if n == 1:
        return 1
    return 2*n-1 + sumNodd(n-1)

def sumNeven(n):
    if n == 1:
        return 2
    return 2*n + sumNeven(n-1)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def sumNsquare(n):
    if n == 1:
        return 1
    return n*n + sumNsquare(n - 1) 

print(sumNsquare(5))