a = 5  # Binary: 0101
b = 3  # Binary: 0011
result = a & b  # Binary: 0001 (Decimal: 1)
print(result)  # Output: 1


a = 5  # Binary: 0101
b = 3  # Binary: 0011
result = a | b  # Binary: 0111 (Decimal: 7)
print(result)  # Output: 7


a = 5  # Binary: 0101
b = 3  # Binary: 0011
result = a ^ b  # Binary: 0110 (Decimal: 6)
print(result)  # Output: 6


a = 5  # Binary: 0101
result = ~a  # Flips bits (depends on system representation)
print(result)  # Output: -6 (Two's complement representation)


a = 5  # Binary: 0101
result = a << 1  # Binary: 1010 (Decimal: 10)
print(result)  # Output: 10


a = 5  # Binary: 0101
result = a >> 1  # Binary: 0010 (Decimal: 2)
print(result)  # Output: 2
