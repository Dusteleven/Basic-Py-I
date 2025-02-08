from math import sqrt

while True:
    n = int(input("Please type in a number: "))
    if n <0:
        print("Invalid number")
    elif n>0:
        print(sqrt(n))
    elif n ==0:
        break
print("Exiting...")
