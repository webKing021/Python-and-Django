x = int(input("Enter num1 : "))
y = int(input("Enter num2 : "))

# method 1 :
x,y=y,x
print(x,y)

# method 2 :
x=x+y
y=x-y
x=x-y
print(x,y)

# method 3 :
x=x*y
y=x/y
x=x/y
print(x,y)