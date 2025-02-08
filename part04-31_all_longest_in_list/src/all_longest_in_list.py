# Write your solution here





def all_the_longest(myList):
    words = []
    curLen = len(myList[0])

    #find longest length
    for w in myList:
        if len(w)>curLen:
            curLen = len(w)
    
    for x in myList:
        if len(x) == curLen:
            words.append(x)

    return words




if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result)

