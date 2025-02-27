"""
Q5. Write a Python program that accepts a student's marks in three 
subjects and prints the grade based on the following conditions:
 Marks > 90: Grade A
 80 < Marks <= 90: Grade B
 70 < Marks <= 80: Grade C
 60 < Marks <= 70: Grade D
 Marks <= 60: Fail
 Input: Three integer marks (e.g., 85, 92, 78)
 Output: Grade B
 """

sub1 = int(input("Enter Mark of Subject One: "))
sub2 = int(input("Enter Mark of Subject Two: "))
sub3 = int(input("Enter Mark of Subject Three: "))

marks = (sub1 + sub2 + sub3) / 3

if marks > 90:
    print("Grade A")
elif marks > 80 and marks <= 90:
    print("Grade B")
elif marks > 70 and marks <= 80:
    print("Grade B")
elif marks > 60 and marks <= 70:
    print("Grade D")
else:
    print("Fail")
