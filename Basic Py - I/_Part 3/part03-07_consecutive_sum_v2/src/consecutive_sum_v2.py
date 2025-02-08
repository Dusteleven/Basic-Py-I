a = int(input("Limit: "))
b=1
str = " "
sum=0

while sum<a:
    if (sum==0):
        str += "1"
    elif (sum!=0):
        str += f" + {b}"
    sum=sum+b 
    b+=1
    


#print(sum)
#str -= f" + {b}"
print(f"The consecutive sum: {str} = {sum}")