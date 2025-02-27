"""
 Q4. Ask a positive number from user. Print from n to 1. 
Example 1:
 Enter a number = 6
 Output:
 6 5 4 3 2 1
 """

user = int(input("Enter a +ve number: "))

i = user

while i >= 1:
    print(i, end= " ")
    i -= 1