# num1 = int(input("Enter the number: "))
# num2 = int(input("Enter the number: "))

# smaller = min(num1, num2)
# gcd = 1

# for i in range(1, smaller + 1):
#     if num1 % i == 0 and num2 % i == 0:
#         gcd = i

# print(f"The GCD of {num1} and {num2} is {gcd}.")


'''or'''


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

while a > 0 and b > 0:
    if a > b:
        a = a % b
    else:
        b = b % a

if a == 0:
    print(f"The GCD is {b}")
else:
    print(f"The GCD is {a}")
