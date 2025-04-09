"""
Case 1
Ask start from user = 3
Ask end from user = 10
3 4 5 6 7 8 9 10

Case 2
Ask start from user = 15
Ask end from user = 9
9 10 11 12 13 14 15
"""

start = int(input("Enter a start number: "))
end = int(input("Enter an end number: "))

if start > end:
    start, end = end, start

i = start
while i <= end:
    print(i, end=" ")
    i += 1
