"""
Q7. Write a Python program that calculates the BMI and classifies it based 
on the following conditions:
 BMI < 18.5: Underweight
 18.5 <= BMI < 24.9: Normal weight
25 <= BMI < 29.9: Overweight
 BMI >= 30: Obesity
 BMI is calculated as weight(kg) / height(m)^2
 Input: Weight in kg and Height in meters (e.g., 70, 1.75)
 Output: Normal weight
 """

weight = float(input("Enter Weight in kg: "))
height = float(input("Enter Height in meter: "))

bmi = weight / (height**2)

if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 24.9:
    print("Normal Weight")
elif 25 <= bmi < 29.9:
    print("Overweight")
else:
    print("Obesity")
