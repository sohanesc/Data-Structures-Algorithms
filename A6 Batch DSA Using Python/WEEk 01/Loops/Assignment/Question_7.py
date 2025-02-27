"""
 Q7. Ask a number from user. Print the multiplication table of that number.
 Example:
 Enter number = 13
 Output:
13 x 1 = 13
 13 x 2 = 26
 13 x 3 = 39
 13 x 4 = 52
 13 x 5 = 65
 13 x 6 = 78
 13 x 7 = 91
 13 x 8 = 104
 13 x 9 = 117
 13 x 10 = 130
 """

user = int(input("Number: "))

i = 1

while i <= 10:
    print(f"{user} x {i} = {user * i}")
    i += 1