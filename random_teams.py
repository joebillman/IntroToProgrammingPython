import random

peeps = [
    "Aaron",
    "Ben",
    "Brandon",
    "Doug",
    "Jake",
    "Jayson",
    "Jeremy",
    "Joe",
    "Josh",
    "Matt",
    "Melissa",
    "Mike",
    "Oksana",
    "Richard",
    "Tony",
    "Warren"
]
length = len(peeps)
curTeam = 1

while(length > 0):
    peep1 = peeps.pop(random.randint(0, len(peeps)-1))
    peep2 = peeps.pop(random.randint(0, len(peeps)-1))
    print("Team :"+str(curTeam)+" "+peep1+" & "+peep2)
    length = len(peeps)
    curTeam += 1