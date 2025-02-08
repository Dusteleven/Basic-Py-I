st=input("Please type in a word: ")
c = input("Please type in a character: ")

d = int((st.find(c)))
e = d+3

if (d>=0) and (e<len(st)):
    print(st[d:e])