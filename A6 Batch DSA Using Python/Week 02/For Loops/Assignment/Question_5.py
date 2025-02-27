"""
Q5. Ask a number from user. Print Yes if that number is a prime number 
else print No.
 Example 1:
 Enter a number = 20
 Output:
 No
 Example 2:
 Enter a number = 19
 Output:
 Yes
 """

n = int(input("Enter a number: "))

for i in range(2, n):
    if n % i == 0:
        print("No")
        break
    else:
        print("Yes")
        break

