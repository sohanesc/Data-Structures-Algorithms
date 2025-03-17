"""
Assignment-18: Simple problems on recursion
1.  Write a recursive function to print first N natural numbers.
2.	Write a recursive function to print first N natural numbers in reverse order.
3.	Write a recursive function to print first N odd natural numbers.
4.	Write a recursive function to print first N even natural numbers
5.	Write a recursive function to print first N odd natural numbers in reverse order
6.	Write a recursive function to print first N even natural numbers in reverse order.
"""

def printN(n):
    if n > 0:
        printN(n-1)
        print(n, end=" ")

def printNreverse(n):
    if n > 0:
        print(n, end=" ")
        printNreverse(n-1)

def printNodd(n):
    if n > 0:
        printNodd(n-1)
        print(2*n-1, end=" ")

def printNeven(n):
    if n > 0:
        printNeven(n-1)
        # print(2*n-1+1, end=" ")
        print(2*n, end=" ")

def printNoddreverse(n):
    if n > 0:
        print(2*n-1, end=" ")
        printNoddreverse(n-1)

def printNevenreverse(n):
    if n > 0:
        print(2*n, end=" ")
        # print(2*n-1+1, end=" ")
        printNevenreverse(n-1)

printNevenreverse(5)