#defined {}

st={}#empty {} taken as dictionary
#if u want to create empty set use set()

print(type(st))
st=set()
print(type(st))

#insertion order not preserved

st={10,11,12,"hai",98.6,11}
print(st)

#indexing doesnot support in set

#updation can be done by another set

st2={50,60}
st.update(st2)
print(st)
#duplicate is not allowed in set

