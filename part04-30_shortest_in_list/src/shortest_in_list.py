# Write your solution here

def shortest(myList):
    word = myList[0]
    curLen = len(myList[0])

    for w in myList:
        if len(w)<curLen:
            word=w
            curLen=len(w)
    return word


if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = shortest(my_list)
    print(result)