# printing square of a given list

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sqlist = list(map(lambda num: num ** 2, lst))
print(sqlist)


#if the number <5 then num-1,if num>5 then num+1

lst=[1,2,3,4,5,6]
numlst=list(map(lambda num: num-1 if num<5 else num+1 ,lst))#if num>5 else num,lst))
print(numlst)
