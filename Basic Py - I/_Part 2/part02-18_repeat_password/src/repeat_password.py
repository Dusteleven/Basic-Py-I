
a=input("Password: ")
b=input("Repeat password: ")
if a==b:
    print("User account created!")

elif a!=b:
    print("They do not match!")
    while True:
        c=input("Repeat password: ")
        if c==a:
            print("User account created!")
            break
        elif c!=a:
            print("They do not match!")
    