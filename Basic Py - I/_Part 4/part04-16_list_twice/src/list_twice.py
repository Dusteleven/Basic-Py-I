# Write your solution here

mylist=[]
ordList=[]

while True:

    n=int(input("New item: "))
    if n==0:
        break
    mylist.append(n)
    ordList=sorted(mylist)
    print(f"The list now: {mylist}")
    print(f"The list in order: {ordList}")
print("Bye!")