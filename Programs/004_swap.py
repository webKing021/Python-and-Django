# swap 2 nums without using 3rd num

# method 1 :
x = 10
y = 15
x,y=y,x
print(x,y)

# method 2 :
x = 10
y = 15
x=x+y
y=x-y
x=x-y
print(x,y)

# method 3 :
x = 10
y = 15
x=x*y
y=x/y
x=x/y
print(x,y)
