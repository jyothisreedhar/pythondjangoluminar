st1={10,20,30,40}
st2={30,40,50,60,70,80}
#union
#10,20,30,40,50,60,70,80
unset=st1.union(st2)
print(unset)#insertion order not preserved
#intersection
inter=st1.intersection(st2)
#30,40
print(inter)
#difference
diff=st1.difference(st2)#remove st2 elements in st1
print(diff)
#assesment
students=["name1","name2","name3","name3"]
failed std=[name1 name2]
create passed stdlst
