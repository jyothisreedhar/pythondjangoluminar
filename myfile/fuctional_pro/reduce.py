# like map and filter the reduce function cannot be directly available
# it can be import from functools

# find the total sum of the given lst


from functools import reduce

lst = [10, 11, 12, 13, 14, 15]

# 10   11  10+11
# 21   12  21+12
# 33   13   33+13
# 46   14   46+14
# 60   15   60+15
sum = reduce(lambda no1, no2: no1 + no2, lst)  #
print("sum:", sum)

# print highest value from the lst

lst = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
high = reduce(lambda no1, no2: no1 if no1 > no2 else no2, lst)
print("high:", high)

# print lowest value from the lst

lst = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
low = reduce(lambda no1, no2: no1 if no1 < no2 else no2, lst)
print("low", low)
