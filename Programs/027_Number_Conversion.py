# Number conversion (binary, octal, hexadecimal)

# Binary to decimal using int()
print("int() on 0b110 : ", int('0b110', 2))

# Hexa-decimal to decimal using int()
print("int() on 0x1A : ", int('0x1A',16))

# ASCII : int to char
a = chr(97)
print(a)

# Char to int
a = 'K'
c = ord(a)
print(c)

# Binary to decimal conversion
s = "10010"
c = int(s, 2)
print("after conversion to integer : ", end = "")
print(c)

# Binary to octal
c = int(s, 8)
print(c)

# Binary to hexa
c = int(s, 16)
print(c)

# Octal to decimal using int()
print("int() on 0o12 : ", int('0o12', 8 ))