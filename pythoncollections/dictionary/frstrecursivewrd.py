#pattern="ABABBACEEFF"
#FIND FRST RECRSV CHARA#A
#highest recursing word
pattern="ABABBACDDEEEFFFF"
dict={}
for ch in pattern:#a,b,a
    if ch not in dict:#a is not in dict a:1
        dict[ch]=1
    else:
       # print(ch,"recursive character")
      #break
       dict[ch]+=1
for key,value in dict.items():  #printing key and value
    print(key," ",value)
print(dict)
#print(dict.get("E"))#dict(get(e)) gives the value of E
#sort dict base of value
data=sorted(dict,key=dict.get,reverse=True)#sorting in ascnding ordr
print(data)







