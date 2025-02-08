# Write your solution here




def phoneBook():#myD: dir):
    myD={}
    while True:
        inp = input("command (1 search, 2 add, 3 quit): ")

        if inp =='1': #search
            name = input("name: ")
            if name in myD:
                print(myD[name])
            else: print("no number")


        elif inp =='2': #add
            name = input("name: ")
            number = input("number: ")
            print("ok!")
            
            myD[name] = number

        
        elif inp =='3':
            print("quitting...")
            break




phoneBook()

#if __name__ == "__main__":
    