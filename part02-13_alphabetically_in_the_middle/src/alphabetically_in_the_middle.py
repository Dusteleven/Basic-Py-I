a=input("1st letter: ")
b=input("2nd letter: ")
c=input("3rd letter: ")

if a<b and a<c:
    if b<c:
        print(f"The letter in the middle is {b}")
    else:
        print(f"The letter in the middle is {c}")
elif b<a and b<c:
    if a<c:
        print(f"The letter in the middle is {a}")
    else:
        print(f"The letter in the middle is {c}")
elif c<a and c<b:
    if a<b:
        print(f"The letter in the middle is {a}")
    else:
        print(f"The letter in the middle is {b}")