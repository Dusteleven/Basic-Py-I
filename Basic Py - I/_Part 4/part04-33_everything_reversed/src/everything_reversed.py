# Write your solution here

def everything_reversed(myList):
    newList=[]
    word=""

    for w in myList:
        newList.append(w[::-1])
    
    newList = newList[::-1]
    return newList


if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = everything_reversed(my_list)
    print(new_list)