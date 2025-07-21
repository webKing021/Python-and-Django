# Exercise 17: Find the sum of the series upto n terms

# Series: 1 + 2 + 3 + 4 + ... + n

n = int(input("Enter a number: "))

# Method 1: Using simple loop
total = 0
for i in range(1, n + 1):
    total = total + i

print(f"Sum of numbers from 1 to {n} is: {total}")

# Method 2: Using formula
easy_total = n * (n + 1) // 2

print(f"Same answer using easy formula: {easy_total}")
