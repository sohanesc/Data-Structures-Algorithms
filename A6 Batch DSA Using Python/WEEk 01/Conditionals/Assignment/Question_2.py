"""
Q2.  Ask a number from user. Print Positive, Negative or Zero.
 Example 1:
 Enter a number = 6
 Output:
 Positive
 Example 2:
 Enter a number = 0
 Output:
 Zero
 Example 3:
 Enter a number = -9
 Output:
 Negative
"""

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")
