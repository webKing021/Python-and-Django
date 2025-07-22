# menu driven programing for Decimal to binary, octal, hexa, 32

ch = 9
while(ch != 5):
    print("Menu")
    print("1. Decimal to Binary")
    print("2. Decimal to Octal")
    print("3. Decimal to Hexa")
    print("4. Decimal to Base-32")
    print("5. Exit")

    ch = int(input("Enter your choice: "))
    
    if(ch == 1):
        num = int(input("Enter decimal number: "))
        print(bin(num))  # Converts to binary
    elif(ch == 2):
        num = int(input("Enter decimal number: "))
        print(oct(num))  # Converts to octal
    elif(ch == 3):
        num = int(input("Enter decimal number: "))
        print(hex(num))  # Converts to hexadecimal
    elif(ch == 4):
        num = int(input("Enter decimal number: "))
        # Custom conversion to base-32
        print("Base-32 conversion requires custom implementation")
    elif(ch == 5):
        print("Exit")
    else:
        print("Invalid choice")
