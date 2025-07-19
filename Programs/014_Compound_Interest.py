# Compound Interest
# Compound Interest = P(1 + r/100)^y - P
# P = Principal amount
# r = Rate of interest
# y = Time period in years

p = 1200
r = 12
y = 3
"""
#To calculate compount interest on amount
amount = p * (1 + 0.01 * r)**y
compound = amount - p
"""
# To calculate total amount
compound = p * (1 + 0.01 * r)**y
print("Compound Interest is:" , round(compound , 2))
