"""
 Q4. Write a Python program that accepts an integer number from the user 
and classifies it as:
 Positive and Even
 Positive and Odd
 Negative and Even
 Negative and Odd
 Zero
 Input: An integer (e.g., -4)
 Output: Negative and Even
 """

num = int(input("Enter a number: "))

if num > 0 and num % 2 == 0:
    print("Positive and Even")
elif num > 0 and num % 2 != 0:
    print("Positive and Odd")
elif num < 0 and num % 2 == 0:
    print("Negative and Even")
else:
    print("Negative and Odd")
