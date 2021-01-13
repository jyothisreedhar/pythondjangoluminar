#you are giving 3 inputs n,min,max find the no of values raised to the nth power
# that lie in the range(min,max) inclusive
---------------------------------------------------------------------------
----------------------------------------------------------------------------



n=int(input('enter the value of n:')) #2
min=int(input('enter the value of min:'))#40
max=int(input('enter the value of max:'))#90
count=0
for i in range(min,max):
    res=i**n
    if(res<=max)|(res>=min):
        count+=1
        print(res)
