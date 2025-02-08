

found = False

while found == False:
    n=input("Editor: ")

    if n.lower() == "visual studio code":
        print("an excellent choice!")
        found = True
    elif n.lower() != "word" and  n.lower() != "notepad":
        print("not good")
        found = False
    else:
        print("awful")
        found = False
