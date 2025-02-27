"""
 Q1. Ask a positive number from user. Print from 1 to n. 
Example 1:
 Enter a number = 6
 Output:
 1 2 3 4 5 6
 """

n = int(input("Enter a number: "))

i = 1

while i <= n:
    print(i, end=" ")
    i += 1