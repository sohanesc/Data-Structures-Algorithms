"""
Sum of 1 to n
"""

n = int(input("Enter a number: "))

total = 0
i = 1
while i <= n:
    print(f"{i}", end=" ")
    total += i
    i += 1

print(f"= {total}")
