number = int(input("Enter the number: "))

reverse = 0
while number > 0:
    remainder = number % 10
    reverse = reverse * 10 + remainder
    number = number // 10

if reverse == number:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")