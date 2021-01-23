# word='HELLO HAI HELLO HAI HELLO'
# WORD COUNT
# HELLO:3,HAI:2
# print(word.count("hello"))
# print(word.count("hai"))
# ------------------
text = "hello hai hello hai hello"
lst = []
words = text.split(" ")  # words=["hello hai hello hai hello"]
print(words)
dict = {}
# key    value

# hai     2
# hello   3

for word in words:  # word=hello,hai,hello
    if (word not in dict):
        dict[word] = 1
    else:
        dict[word] += 1  # dict["hello] 1+1=2
print(dict)
