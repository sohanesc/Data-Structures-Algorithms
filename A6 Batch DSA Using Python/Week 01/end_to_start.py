"""
Ask end, Ask start and return the numbers
"""

start = int(input("Enter a start number: "))
end = int(input("Enter a end number: "))

i = end

while i >= start:
    print(i, end=" ")
    i -= 1
