n = input("Enter a number: ")

def sum_first_n_nums(n):
    if n == 0:
        return 0
    else:
        return n + sum_first_n_nums(n - 1)

print(sum_first_n_nums(int(n)))