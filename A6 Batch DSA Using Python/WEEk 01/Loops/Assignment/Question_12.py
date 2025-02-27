"""
 Q12. Print the following pattern. Ask n from user.
 Example 1:
 Enter n = 5
 Output:
 1 11 111 1111 11111
 Example 1:
 Enter n = 7
 Output:
 1 11 111 1111 11111 111111 1111111
 """

n = int(input("Enter number: "))

i = 1
num = 1

while i <= n:
    print(num, end=" ")
    num = num * 10 + 1
    i += 1