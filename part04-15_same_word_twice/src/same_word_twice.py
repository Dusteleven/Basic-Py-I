# Write your solution here

mylist=[]

once= True

while once==True:
    s=input("Word: ")
    mylist.append(s)
    i=0

    while len(mylist)!= 1 and (i<len(mylist)-1):
        
        if s == mylist[i]:
            once = False
            break
        i+=1

print(f"You typed in {len(mylist)-1} different words")