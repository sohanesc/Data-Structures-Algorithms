decimal = int(input("enter a Decimal number: "))


def convert2Binary(decimal):
    result = " "
    while decimal > 0:
        if decimal % 2 == 1:
            result += "1"
        else:
            result += "0"
        decimal = decimal // 2
    result = result[::-1]
    return result


print(convert2Binary(decimal))
