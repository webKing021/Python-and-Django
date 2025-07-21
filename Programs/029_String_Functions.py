# str(), eval(), repr() functions

# str() function
a = 21
print(str(a))  # Converts integer to string

# eval() function - works while provided statement is valid
eval('7+7+7')
eval("20==21")  
x = 2
y = 3
eval('x+y')  # Evaluates the expression using variables in current scope

# repr() function - raw text or raw print
x = "krutarth\n21"
print(repr(x))  # Shows escape sequences as they are

print("\het\ne3")  # \h is not a valid escape sequence, so it prints as is