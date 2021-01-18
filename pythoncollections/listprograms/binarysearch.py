#binary search

lst=[10,8,7,11,12,6,5]
#sorting lst
lst.sort()
flag=0
#print(lst)
low=0
upp=len(lst)-1
element=int(input("enter the element for search"))
while(low<=upp):
    mid=(low+upp)//2
    if(element>lst[mid]):
        low=mid+1
    elif(element<lst[mid]):
        upp=mid-1
    elif(element==lst[mid]):
        flag+=1
        break
if flag==0:
    print("element not found")
else:
    print("element found")
