st=input("Please type in a word: ")
c = input("Please type in a character: ")

i=0

while i<(len(st)-2):
    if st[i]==c:
        print (st[i:i+3])
    i+=1