# find the squre of the given list

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sqlst = list(map(lambda num: num ** 2, lst))  # 2^2
print("sqlst:", sqlst)

# print the list if the num<5,num-1 if num>5 num+1#if===>else

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numlst = list(map(lambda num: num - 1 if num < 5 else num + 1, lst))
print("numlst:", numlst)

# using elif

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_lst = list(map(lambda num: num - 1 if num < 5 else num + 1 if num > 5 else num, lst))
print("num_lst:", num_lst)

# covert the given names into uppercase

names = ["india", "srilanka", "pakisthan", "afganisthan", "europe", "italy", "africa"]
uplst = list(map(lambda name: name.upper(), names))
print("uplst:", uplst)

# covert the given names into lowercase

name=['INDIA', 'SRILANKA', 'PAKISTHAN', 'AFGANISTHAN', 'EUROPE', 'ITALY', 'AFRICA']
lowlst=list(map(lambda name:name.lower(),name))
print("lowlst:",lowlst)
