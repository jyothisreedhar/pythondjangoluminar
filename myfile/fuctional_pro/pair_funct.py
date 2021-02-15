#given that
#lst1=[1,2,3,4]
#lst2=[5,6,7,8]
#make(1,5),(1,6),(1,7),(1,8),,,,,....all pairs

lst1=[1,2,3,4]
lst2=[5,6,7,8]
#for i in lst1:#1
   # for j in lst2:#5
       # print((i,j))#(1,5)
output=[(i,j)for i in lst1 for j in lst2]
print(output)