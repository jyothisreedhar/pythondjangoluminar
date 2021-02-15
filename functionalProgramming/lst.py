# given that
# list1=[1,2,3,4]
# list2=[2,4,5,6,7,8]
# find the common elements using functional programming


list1=[1,2,3,4]
list2=[2,4,5,6,7,8]
out_lst=list(filter(lambda num:num in list1,list2))
print(out_lst)
