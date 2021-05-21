test_str="geeksforgeeks" #initialize the string

print("the string is",test_str)  #print the string
all_freq={} #
#print(all_freq)

for i in test_str: #geeksforgeeks
    if i in all_freq:#g,e
        all_freq[i]+=1 #g=1,e=1
        print(all_freq)
    else:
        all_freq[i]=1 #e=2
        print(all_freq)
res=max(all_freq,key=all_freq.get)
print("the maximum occuring character is:",str(res))