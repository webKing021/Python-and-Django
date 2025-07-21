# Exercise 14: Reverse a given integer number

num = int(input("Enter a number: "))

# Convert number to string, reverse it, and convert back to integer
reversed_num = int(str(num)[::-1])
print("Reversed number:", reversed_num)
