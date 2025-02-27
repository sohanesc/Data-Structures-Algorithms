# Write a Python script to create a list of the first N terms of a Fibonacci series.


def fibonacci(N):
    fib_sequence = [0, 1]
    while len(fib_sequence) < N:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:N]


N = 10
fibonacci_list = fibonacci(N)
print(f"First {N} terms of Fibonacci series:", fibonacci_list)
