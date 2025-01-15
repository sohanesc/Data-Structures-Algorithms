n = input("Enter a number: ")

def print_one2n(n):
    if n == 1:
        print(n)
    else:
        print_one2n(n-1)
        print(n)

print_one2n(int(n))