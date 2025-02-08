st = input("Please type in a string: ")
c1 = st[1]
c2 = st[len(st)-2]

if c1 == c2:
    print(f"The second and the second to last characters are {c1}")
else:
    print("The second and the second to last characters are different")