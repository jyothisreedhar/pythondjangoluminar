# find yera vise released movies
f = open("movies.csv", "r")
dict = {}
for lines in f:
    data = lines.rstrip("\n").split(",")
    # print(data)
    # break
    #movie = data[1]
    year = data[2]
    if (year not in dict):
        dict[year] = 1
    else:
        dict[year] += 1
print(dict)
for key, value in dict.items():
    print(key, " ===>", value)
result=sorted(dict,key=dict.get,reverse=True)
print(result[0],"====>",dict.get(result[0]))
#print(result[0]),dict.get(result[0])
