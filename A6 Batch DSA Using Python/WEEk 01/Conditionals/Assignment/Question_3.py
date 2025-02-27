"""
 Q3.  Ask a number from user. Print Yes if the number is divisible by 2,3 and 5.
 Example 1:
 Enter a number = 30
Output:
 Yes
 Example 2:
 Enter a number = 6
 Output:
 No
 """

num = int(input("Enter a number: "))

if num % 2 == 0 and num % 3 == 0 and num % 5 == 0:
    print("Yes")
else:
    print("No")
