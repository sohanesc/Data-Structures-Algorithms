"""
Keep on asking a integer from the user. Until he enters 0
Enter a number: 5
Enter a number: 6
Enter a number: 7
Enter a number: 8
Enter a number: 9
Enter a number: 0
Sum of all numbers entered
"""

total = 0
count = 0

while True:
    num = int(input("Enter a number: "))
    if num == 0:
        break
    total += num
    count += 1

print(f"Total number is {total} & Average is {total/count}")
