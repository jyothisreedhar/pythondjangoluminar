# create student set
std = open("students", "r")  # open stud file
std_lst = set()  # create a EMPTY SET of std file
for lines in std:  # read file line by line
    s_word = lines.rstrip("\n")  # gives the file by eliminate the\n
    std_lst.add(s_word)  # add this  in to empty set
print("student name:", std_lst)
# create failed student set
failstd = open("fail","r")
fail_lst=set()
for lines in failstd:
    f_word=lines.rstrip("\n")
    fail_lst.add(f_word)
print("failed student:",fail_lst)
pas_std=std_lst.difference(fail_lst)
print("passed students:",pas_std)



# print(std_word)  # print the list

# create failed student list repeating the same procedure

# fail_word = []
# for lines in failstd:
# print(lines)
# word=lines.rstrip("/n")
# print(word)
# fail_word.append(lines.split(" "))
# print(fail_word)
