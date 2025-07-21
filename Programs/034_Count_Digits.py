# Exercise 6: Count the total number of digits in a number

num = int(input("Enter a number: "))

# Simply convert number to string and count length
digits = len(str(num))
print(f"Number {num} has {digits} digits")
