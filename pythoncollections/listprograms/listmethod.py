#how to create empty lst
#lst=[]
lst=list()#creating an empty list
#method for adding element in a list
#list.append()
#print 1 to 50

for i in range(1,51):
    lst.append(i)
print(lst)

#total sum
total=sum(lst)
print(total)
#print highest element
high=max(lst)
print(high)
min=min(lst)
print(min)