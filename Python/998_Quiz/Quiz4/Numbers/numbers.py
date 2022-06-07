mynumbers = [6,9,32,28,15,22,3,18]

min = mynumbers[0]
for i in range(0, len(mynumbers)):
    if(mynumbers[i] < min):
        min = mynumbers[i]
print("Minimum: " + str(min))

max = mynumbers[0]
for i in range(0, len(mynumbers)):
    if(mynumbers[i] > max):
        max = mynumbers[i]
print("Maximum: " + str(max))

avg = 0
for i in range(0, len(mynumbers)):
    avg = avg + mynumbers[i]
avg = avg/len(mynumbers)
print("Average: " + str(avg))
