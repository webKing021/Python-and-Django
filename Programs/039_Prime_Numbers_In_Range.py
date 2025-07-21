# Exercise 11: Write a program to display all prime numbers within a range

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print(f"Prime numbers between {start} and {end} are:")

for num in range(start, end + 1):
    if num > 1:
        prime = True
        # Check if number is divisible by anything up to its square root
        for i in range(2, num):
            if num % i == 0:
                prime = False
                break
                
        # Print if prime
        if prime:
            print(num, end=" ")
