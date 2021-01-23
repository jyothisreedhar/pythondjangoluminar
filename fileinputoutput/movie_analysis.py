f=open("movies.csv","r")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    movie=data[1]
    year=data[2]
    if(movie not in dict):
        dict[movie]=year
    else:
        dict[movie]=year
for key,value in dict.items():
    print(key," ===>",value)