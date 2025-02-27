n = input("Enter a number: ")

def print_n_times(n):
    if n == 0:
        return
    print("Hello")
    print_n_times(n - 1)

print_n_times(int(n))