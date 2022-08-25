print(sum([x for x in range(1000) if x % 3 == 0 or x % 5 == 0]))

#   Without list comprehension
nums = []
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        nums.append(i)

sum_of_numbs = sum(nums)
print(sum_of_numbs)