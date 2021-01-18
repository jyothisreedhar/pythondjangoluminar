#THE GIVEN LIST IS
#lst=[2,6,4] => and the o/p in the format of [10,6,8]
#lst=[3,4,5] amd the o/p=>[9,8,7]
lst=[2,5,6,7]# o/p [18,15,14,13]

#step1=> finding total of the list
#total=20
#[]
#20-2=18,20-5=15
out=list()
total=sum(lst)
for num in lst:
    out.append(total-num)
print(out)
