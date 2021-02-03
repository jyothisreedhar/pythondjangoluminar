# covid data analysis
f = open("covid_19_india.csv", "r")
dict = {}
for lines in f:
    data = lines.rstrip("\n").split(",")
    # print(data)
    # break

    # state confirmed cases
    state = data[3].rstrip("***")
    if(state=="Telengana"):
        state="Telangana"
    confirmed_cases = int(data[8])
    if ( state not in dict ):#if kerala not in dict
        dict[state] = confirmed_cases
    else:
        dict[state] = confirmed_cases
for key, value in dict.items():
    print(key, "====>", value)
result=sorted(dict, key=dict.get, reverse=True)#decse-h-l
print(result[0],dict.get(result[0]))