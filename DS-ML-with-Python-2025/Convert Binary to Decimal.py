def binary_to_decimal(binary_str):
    decimal = 0
    power = 0

    for digit in reversed(binary_str):
        if digit == '1':
            decimal += 2 ** power
        power += 1

    return decimal

binary_input = input("Enter binary number: ")
print("Decimal equivalent:", binary_to_decimal(binary_input))
