"""
Q6. Write a program to find the maximum and minimum of three numbers 
entered by the user using if-else statements.
 Input: Three integers (e.g., 3, 9, 5)
 Output: Max is 9 and Min is 3
 """

num1 = int(input("Enter number 1 = "))
num2 = int(input("Enter number 2 = "))
num3 = int(input("Enter number 3 = "))

# Find maximum
if num1 >= num2 and num1 >= num3:
    maximum = num1
elif num2 >= num1 and num2 >= num3:
    maximum = num2
else:
    maximum = num3

# Find minimum
if num1 <= num2 and num1 <= num3:
    minimum = num1
elif num2 <= num1 and num2 <= num3:
    minimum = num2
else:
    minimum = num3

print(f"Max is {maximum} and Min is {minimum}")
