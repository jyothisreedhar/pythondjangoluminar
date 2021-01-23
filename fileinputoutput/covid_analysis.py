#covid data analysis
f=open("covid_19_india.csv","r")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    #state confirmed cases
    state=data[3].rstrip("***")
    if(state=="Telengana"):
        state="Telengana"
    confirmed_cases=int(data[8])
    if (state not in dict):
        dict[state]=confirmed_cases
    else:
        dict[state]=confirmed_cases
f