a=int(input("Number 1: "))
b=int(input("Number 2: "))
ops = input("Operation: ")

if ops == "add":
    print(f"{a} + {b} = {a+b}")
if ops == "subtract":
    print(f"{a} - {b} = {a-b}")
if ops == "multiply":
    print(f"{a} * {b} = {a*b}")