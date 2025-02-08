# Write your solution here

def formatted(myList):
    newList=[]
    for x in myList:
        newList.append(f"{x:.2f}")
    return newList
    



if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)