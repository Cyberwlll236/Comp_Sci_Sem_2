import random
thislist = []
num1 = int(input("How many random numbers would you like? "))
for x in range(0,num1):
    thislist.append(random.randrange(9))
print(thislist)