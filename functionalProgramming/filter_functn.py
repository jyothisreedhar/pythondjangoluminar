# extract even numbers from the given list


lst=[1,2,3,4,5,6,7,8,9,10]
even_lst=list(filter(lambda num:num%2==0,lst))
print(even_lst)

## extract odd numbers from the given list

lst=[1,2,3,4,5,6,7,8,9,10]
odd_lst=list(filter(lambda num:num%2!=0,lst))
print(odd_lst)
