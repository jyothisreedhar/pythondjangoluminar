# print name staring with "a

names = ["india", "pak", "aus", "eng", "china", "srilanka", "auklnd", "indonesia"]
a_country = list(filter(lambda name: name[0] == "a", names))
print(a_country)
