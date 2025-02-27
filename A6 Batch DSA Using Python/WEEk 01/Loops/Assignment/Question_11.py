"""
Q11. Print the following pattern. Ask n from user.
 Example 1:
 Enter n = 6
 Output:
 1 2 4 8 16 32
 Example 1:
 Enter n = 10
 Output:
 1 2 4 8 16 32 64 128 256 512
"""

n = int(input("Enter number: "))

i = 1
num = 1

while i <= n:
    print(num, end = " ")
    num *= 2
    i+=1