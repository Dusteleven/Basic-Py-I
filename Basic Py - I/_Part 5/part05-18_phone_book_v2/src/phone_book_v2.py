# Write your solution here
# Write your solution here




def phoneBook():#myD: dir):
    myD={}
    while True:
        inp = input("command (1 search, 2 add, 3 quit): ")

        if inp =='1': #search
            name = input("name: ")
            if name in myD:
                for n in myD[name]:
                    print(n)
            else: print("no number")


        elif inp =='2': #add
            name = input("name: ")
            number = (input("number: "))
            print("ok!")
            if name in myD:
                myD[name].append(number)
            else:
                myD[name] = [number]

        
        elif inp =='3':
            print("quitting...")
            break




phoneBook()
#2
#mary
#040-234567
#1
#mary
#3



#if __name__ == "__main__":
    