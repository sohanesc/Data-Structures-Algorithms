"""
Ask a number from user

if number divisible by 2 -> FIZZ
if number divisible by 3 -> BUZZ
if number divisible by 2 and 3 -> FIZZBUZZ
else:
FIZZBUZZFIZZBUZZ
"""

num = int(input("Enter number = "))

if num % 2 == 0:
    print("FIZZ")
if num % 3 == 0:
    print("BUZZ")
if num % 2 and num % 3:
    print("FIZZBUZZ")
else:
    print("FIZZBUZZFIZZBUZZ")
