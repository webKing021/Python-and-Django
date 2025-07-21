# Exercise 3: Calculate the sum of all numbers from 1 to a given number

num = int(input("Enter a number: "))
sum = 0

for i in range(1, num + 1):
    sum = sum + i

print(f"Sum of numbers from 1 to {num} is: {sum}")