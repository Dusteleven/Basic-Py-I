# Write your solution here


def printter(myList: list):
    for i in range(len(myList)):
          print(f"{myList[i]}", end="")
    print()


layers = int(input("Layers: ")) #layers 3, lines 5

#layers=5

lines=[0,1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51]
half=[0,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
letters = "AABCDEFGHIJKLMNOPQRSTUVWXYZ"

if layers ==1: print("A")

elif layers !=0:

    printLayer=[]
    for i in range(lines[layers]):
        printLayer.append(letters[layers]) #print layer starts with all one letter (max layer)

    a=0
    b=(lines[layers])-1
    c=layers-1
    printter(printLayer)

    #start decreasing
    #letters = "AABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(half[layers],0,-1): #layers+2)/2)+1
    
            for j in range(a+1,b,1): #change inside of print layer
                printLayer[j]=letters[c]
                
            printter(printLayer)

            b-=1
            a+=1
            if a!=b:
                c-=1
    a-=1
    b+=1
    c+=1

    for i in range(half[layers]): #layers+2)/2)+1
  
        for j in range(a+1,b,1): #change inside of print layer
            printLayer[j]=letters[c]
                
        printter(printLayer)
        b+=1
        c+=1
        a-=1




    
