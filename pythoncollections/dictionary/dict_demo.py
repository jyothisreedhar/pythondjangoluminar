#object are stored in dict in the form of key value pair
#we fetch value from dictionary using key
#impossible to store duplicate values
#key must be unique
-------------------------------
expenses={"jan20":30000,"feb20":6000,"march20":28000,"april20":8000,"may20":6700}
print("june20" in expenses)
#adding new key value pairs
--------------------------------
#june20,25000
expenses["june20"]=25000
print(expenses)
print("march20" in expenses)
expenses["march20"]-=3000
print(expenses["march20"])
