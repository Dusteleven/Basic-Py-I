st = input("Please type in a string: ")
c = input("Please type in a substring: ")


loc1=st.find(c)
loc2=-1
if loc1!=-1:
    loc2=st.find(c,loc1+len(c))
if loc2 != -1:
    print(f"The second occurrence of the substring is at index {loc2}.")
else:
    print("The substring does not occur twice in the string.")




