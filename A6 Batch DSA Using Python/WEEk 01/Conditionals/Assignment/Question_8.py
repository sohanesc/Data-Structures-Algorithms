"""
Q8. Write a Python program to determine if a student is eligible for college 
admission based on the following criteria:
 Minimum score in Math: 70
 Minimum score in Science: 65
 Minimum score in English: 60
 Total score across all subjects: 200
 Input: Three scores (e.g., 75, 70, 65)
 Output: Eligible for Admission
 """

math = int(input("Enter Math number: "))
science = int(input("Enter Science number: "))
english = int(input("Enter English number: "))

total = math + science + english

if math >= 70 and english >= 65 and english >= 60 and total >= 200:
    print("Eligible for Admission")
else:
    print("Not Eligible for Admission")
