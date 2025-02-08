# Write your solution here

mylist=[]
print(f"The list is now {mylist}")
i=0

while True:

    inp = input("a(d)d, (r)emove or e(x)it: ")
    if inp == "d":
        mylist.append(i+1)
        print(f"The list is now {mylist}")
        i+=1
    elif inp == "r":
        mylist.pop(i-1)
        print(f"The list is now {mylist}")
        i-=1
    elif inp == "x":
        break
print("Bye!")
    