total = int(0)
num1 = int(input("How many items do you want to buy? "))
for x in range(0,num1):
    item = input("What item are you buying? ")
    cost = int(input("How much does it cost? $"))
    total = total + cost
print("Your total is $" + str(total))