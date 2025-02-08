
count = 0
sum = 0
pos = 0
neg = 0

print("Please type in integer numbers. Type in 0 to finish.")

while True:
    n = int(input("Number: "))
    if n==0:
        break
    count += 1
    sum = sum + n
    if n>0:
        pos += 1
    if n<0:
        neg += 1
print(f"... the program asks for numbers\nNumbers typed in {count}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {sum/count}")
print(f"Positive numbers {pos}")
print(f"Negative numbers {neg}")
    

