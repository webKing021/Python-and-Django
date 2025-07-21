# User input: decimal to binary, octal, and hexadecimal

# Decimal to binary, octal, and hexadecimal
n = int(input("enter decimal num : "))
print("binary : ", bin(n))
print("octal : ", oct(n))
print("hexa : ", hex(n))

# Binary to binary, octal, hexadecimal, and base 32
n = (input("enter binary num : "))
print("binary : ", int(n, 2))
print("octal : ", int(n, 8))
print("hexa : ", int(n, 16))
print("32 : ", int(n, 32))