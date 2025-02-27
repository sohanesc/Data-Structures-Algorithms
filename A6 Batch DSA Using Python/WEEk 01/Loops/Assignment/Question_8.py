"""
Q8. Ask a start number and end number from user. Ask another number n 
from the user. Print all the numbers from start to end divisible by n.
 Example 1:
 Enter start = 50
 Enter end = 192
 Enter n = 13
 Output:
 52 65 78 91 104 117 130 143 156 169 182
 Example 2:
 Enter start = 1
 Enter end = 100
 Enter n = 24
 Output:
 24 48 72 96
 """

start = int(input("Start Number: "))
end = int(input("End Number: "))
n = int(input("n Number: "))

i = start

while i <= end:
    if i % n == 0:
        print(i, end = " ")
    i += 1