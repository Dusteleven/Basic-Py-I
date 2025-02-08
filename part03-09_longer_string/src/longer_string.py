s1 = input("Please type in string 1: ")
s2 = input("Please type in string 2: ")
l1 = len(s1)
l2 = len(s2)

if l1>l2:
    print(f"{s1} is longer")
elif l2>l1:
    print(f"{s2} is longer")
else:
    print("The strings are equally long")