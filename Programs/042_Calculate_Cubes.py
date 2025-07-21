# Exercise 16: Calculate the cube of all numbers from 1 to a given number

num = int(input("Enter a number: "))

for i in range(1, num + 1):
    cube = i * i * i
    print(f"{i} cubed is {cube}")
