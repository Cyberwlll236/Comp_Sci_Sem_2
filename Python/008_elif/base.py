num1 = int(input("Please enter a number: "))
op = input("Please input an operation: ")
num2 = int(input("Please enter a number: "))
print("")
if op == "+":
    print(str(num1) + op + str(num2) + " = " +str(num1+num2))
elif op == "-":
    print(str(num1) + op + str(num2) + " = " +str(num1-num2))
elif op == "*":
    print(str(num1) + op + str(num2) + " = " +str(num1*num2))
elif op == "/":
    print(str(num1) + op + str(num2) + " = " +str(num1/num2))
else:
    print("Please input a valid operation.")