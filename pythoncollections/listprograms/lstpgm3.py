lst=[10,11,12,13,14,15,16,17]
#store even numbers to=>evenlst
#store odd numbers to=>oddlst
#find total of evenlist,oddlist
evnlist=list()
oddlist=list()
for num in lst:
    if (num%2==0):
        evnlist.append(num)
    else:
        oddlist.append(num)
print(oddlist)
print(evnlist)
print("oddsum",sum(oddlist))
print("evnsum",sum(evnlist))