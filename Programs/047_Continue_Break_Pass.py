# continue -> loop back

for i in range(2, 10):
    if(i % 2 == 0):
        print(f"{i} is even number")
        continue # continue to next iteration
        num = 3
print(i)

# break -> loop break
for i in range(2, 10):
    if(i % 2 == 0):
        print(f"{i} is even number")
        break # break loop
        num = 3
print(i)

# pass -> do nothing
for i in range(2, 10):
    if(i % 2 == 0):
        print(f"{i} is even number")
        pass # do nothing
        num = 3
print(i)
