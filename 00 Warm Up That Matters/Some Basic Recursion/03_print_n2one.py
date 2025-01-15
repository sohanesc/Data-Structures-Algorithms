n = input("Enter a number: ")

def print_n2one(n):
    if n == 0:
        return
    print(n)
    print_n2one(n-1)

print_n2one(int(n))