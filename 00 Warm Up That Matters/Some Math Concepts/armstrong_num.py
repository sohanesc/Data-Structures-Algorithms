number = int(input("Enter the number: "))

# Store the original number
original_number = number

num = len(str(number))
sum = 0

while number > 0:
    remainder = number % 10
    sum += remainder ** num
    number = number // 10

if sum == original_number:
    print(f"The number {original_number} is an Armstrong number.")
else:
    print(f"The number {original_number} is not an Armstrong number.")
