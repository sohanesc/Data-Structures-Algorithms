num = int(input("Enter a number: "))
divisors = []

for i in range(1, int(num**0.5) + 1):  # +1 to include the square root
    if num % i == 0:
        divisors.append(i)
        if num // i != i:  # to avoid duplicates
            divisors.append(
                num // i
            )  # if the number is not a perfect square, then add the square root


divisors.sort()
print(*divisors)  # * means unpacking divisors for printing
print("The number of factors is", len(divisors))
