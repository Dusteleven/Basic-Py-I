


mylist=[1,2,3,4,5]
ind=1

while ind != -1:
    ind=int(input("Index: "))
    if ind == -1:
            break
    nVal=int(input("New value: "))
    mylist[ind]=nVal
    print(mylist)
