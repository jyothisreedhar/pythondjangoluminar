# extract even numbers from the given list

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evenlst = list(filter(lambda num: num % 2 == 0, lst))
print("evenlst:", evenlst)

# extract odd numbers from the given list
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
oddlst = list(filter(lambda num: num % 2 != 0, lst))
print("oddlst:", oddlst)

# print country whose name start with a

names = ["india", "srilanka", "pakisthan", "afganisthan", "europe", "italy", "africa","australia"]
a_name=list(filter(lambda name:name[0]=="a",names))
print("a_name:",a_name)