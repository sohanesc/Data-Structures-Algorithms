"""
Q9. Count the number of odd and even numbers from start to end. Ask 
start and end number from user.
 Example 1:
 Enter start = 1
 Enter end = 100
 Output:
 Even = 50
 Odd = 50
 """

start = int(input("Start Number: "))
end = int(input("End Number: "))

even = 0
odd = 0

i = start

while i <= end:
    if i % 2:
        even += 1
    else:
        odd += 1
    i += 1

print(f"Even = {even} & Odd = {odd}")