# 

pattern = input("Enter the pattern: ")
rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    print(f"{pattern * i}")
