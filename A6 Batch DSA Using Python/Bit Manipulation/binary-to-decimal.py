binary = str(input("enter a Binary number: "))


def convert2Decimal(binary):
    result = 0
    power = 0
    index = len(binary) - 1
    while index >= 0:
        num = int(binary[index]) * (2**power)
        result += num
        index -= 1
        power += 1
    return result


print(convert2Decimal(binary))
