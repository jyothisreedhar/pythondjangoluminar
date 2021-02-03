from typing import Dict

f = open("covid_19_india.csv", "r")
covid = {}
for lines in f:
    data = lines.rstrip("\n").split(",")
    state = data[3]
    cured = data[6]
    death = data[7]
    confirmed = data[8]
    if state not in covid:
        covid[state] = {"state": state, "cured": cured, "death": death, "confirmed": confirmed}
    else:
        covid[state] = {"state": state, "cured": cured, "death": death, "confirmed": confirmed}
print(covid)

def print_covid_data(**kwargs):
    state = kwargs["state"]
    if state in covid:
        print(covid[state]["state"])
        if "prop" in kwargs:
            prop = kwargs["prop"]
            print(covid[state][prop])
        else:
            pass
    else:
        print("the mentioned state doent exist")




print_covid_data(state="kerala", prop="death")
