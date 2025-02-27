# Write a Python script to create a list of the first N prime numbers.


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def first_n_primes(N):
    primes = []
    num = 2
    while len(primes) < N:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes


N = 10
primes_list = first_n_primes(N)
print(f"First {N} prime numbers:", primes_list)
