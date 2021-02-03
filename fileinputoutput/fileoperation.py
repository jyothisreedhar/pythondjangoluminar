# file operations are read ,write, append
# step1 reading---we have to create referenc
# f=open("filepath","mode")#
f = open("demo", "r")#open the file and read it
word = []
for lines in f:  # iterate the file line by line(this is)
    words = lines.split(" ")  # split he file by providing sapce(this,is) it
    for wrd in words:
        word.append(wrd.rstrip("\n"))
# word.append(lines.rstrip("\n ").split(" "))
print(word)
# words=word.lines.split(" ")

# highest repeating word from file(word count):dict
dict={}
for line in word:
    if (line not in dict):
        dict[line]=1
    else:
        dict[line]+=1
for key,value in dict.items():#used for getting the key value
    print(key,value)
result=sorted(dict, key=dict.get, reverse=True)
print(result)
print(result[0],dict.get(result[0]))