n = input("Enter you first and last name: ")
space = ""
for i in range(0,len(n)):
    print(n[i:i+1])
    if i == " ":
        space = int(i)
print(n[space:len(n)])
print(n[0:space])