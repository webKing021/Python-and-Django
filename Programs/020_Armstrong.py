# Armstrong Number

num = int(input("Enter a number: "))

sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum += digit * digit * digit
    temp = int(temp / 10)  # Using normal division and converting to int

if num == sum:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
