# Exercise 15: Use a loop to display elements from a given list present at odd index positions

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# odd index
for position in range(1, len(nums), 2):
    print(nums[position])
