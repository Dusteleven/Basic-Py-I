st=input("Please type in a sentence: ")

print(st[0])
j=0


while j< len(st):
    if st[j] == " ":
        print (st[j+1])
    j+=1