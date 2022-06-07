peoplelist = []
complist = []

with open('People.txt') as f:
    for line in f:
        l = line.strip()
        peoplelist.append(l)

with open('Compliment.txt') as f:
    for line in f:
        l = line.strip()
        complist.append(l)



import random
peoplenum = random.randrange(0, len(peoplelist))
compnum = random.randrange(0, len(complist))

print(peoplelist[peoplenum] + " " + complist[compnum])