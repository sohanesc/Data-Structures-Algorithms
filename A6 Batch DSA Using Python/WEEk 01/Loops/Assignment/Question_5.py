"""
 Q5. Ask a positive number from user. Print from n to -n. 
Example 1:
 Enter a number = 6
 Output:
 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6
 """

user = int(input("A +ve number: "))

i = user

while i >= -user:
    print(i, end = " ")
    i -= 1