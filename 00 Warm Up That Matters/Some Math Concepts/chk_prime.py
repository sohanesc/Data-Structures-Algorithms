number = int(input("Enter the number: "))

prime = True

for i in range(2, number):
    if number % i == 0:
        prime = False
        break

if prime:
    print("Prime")
else:
    print("Not Prime")