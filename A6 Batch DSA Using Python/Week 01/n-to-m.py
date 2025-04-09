n = int(input("Enter init number: "))
m = int(input("Enter exit number: "))

i = n
while i <= m:
    print(i, end=" ")
    print(f"at memory location -> {id(i)}")
    i += 1

print(f"Memory location of M -> {id(m)}")
