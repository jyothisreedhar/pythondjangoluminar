#he given list is
#LST=[1,2,3,4,5] assume we want the pairs of 6
#then grouping like (1,5),(4,2),
#the pairs of 7 like(3,4),(5,2)
#lst=[1,2,3,5]
#num=int(input("enter the number to find pairs:"))
#for i in range(0,len(lst)):
 #   for j in range(i+1,len(lst)):
 #       if(lst[i]+lst[j]==num):
 #           print(lst[i],lst[j])

 #using binary search
lst = [1,2,3,5,9,7,8,10,4,6]
lst.sort()
print(lst)
element = int(input("enter the element want to make pairs :"))#5
low = 0
up = len(lst)-1
while (low<=up):#0<3
    if lst[low]+lst[up]>element:#(1+5=6<5
        up=up-1
    elif lst[low]+lst[up]<element:#gr
        low=low+1
    elif lst[low]+lst[up]==element:
        print("the pairs are:",lst[low],lst[up])
        up=up-1
        low=low+1
