num = int(input("Enter a number: "))
count = 0

for i in range(1, int(num**0.5) + 1):  # +1 to include the square root
    if num % i == 0:
        count += 1
        if num // i != i:  # to avoid duplicates
            count += 1
            if count > 2:
                break

if count == 2:
    print("It is a prime number")
else:
    print("It is not a prime number")
