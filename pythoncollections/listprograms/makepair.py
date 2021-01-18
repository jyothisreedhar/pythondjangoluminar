#he given list is
#LST=[1,2,3,4,5] assume we want the pairs of 6
#then grouping like (1,5),(4,2),
#the pairs of 7 like(3,4),(5,2)
lst=[1,2,3,5]
num=int(input("enter the number to find pairs:"))
for i in range(0,len(lst)):
    for j in range(i+1,len(lst)):
        if(lst[i]+lst[j]==num):
            print(lst[i],lst[j])