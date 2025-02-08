n=int(input("Please type in a number: "))
i=1


while i<=n:
    j=1
    while j<=n:
        print(f"{i} x {j} = {i*j}")
        j+=1
    i+=1
