# Fibonacci

num = int(input("Enter the number of terms: "))

n1 = 0 
n2 = 1

for i in range(num): # Loop from 0 to (num - 1)
    print(n1)   # Print current term
    n1, n2 = n2, n1 + n2 # Update n1 and n2
