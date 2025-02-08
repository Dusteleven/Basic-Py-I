n = 1

while n > 0:
    fact=1
    n = int(input("Please type in a number: "))

    if n<=0:
        break
    i=2
    while i<=n:
        fact = fact*i
        i+=1
    print(f"The factorial of the number {n} is {fact}")



print("Thanks and bye!")