l = int(input("Please enter line length: "))
a = input("Do you want a vertical or horizontal line: ")
print("")
if a == "horizontal":
    for x in range(0,l):
        print("*", end="")
elif a == "vertical":
    for x in range(0,l):
        print("*")
