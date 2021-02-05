#sum of the given list


from functools import reduce
lst=[10,11,12,13,14]
sum=reduce(lambda no1,no2:no1+no2,lst)#10,11==>10+11=21,21,12=21+12=33,33 13=33+13
print(sum)
low=reduce(lambda no1,no2:no1 if no1<no2 else no2,lst)
print(low)
high=reduce(lambda no1,no2:no2 if no1<no2 else no1,lst )
print(high)