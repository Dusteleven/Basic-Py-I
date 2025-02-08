# Write your solution here


q=int(input("How many items: "))
mylist=[]
i=1
while i <= q:
    j=int(input(f"Item {i}: "))
    mylist.append(j)
    i+=1
print(mylist)