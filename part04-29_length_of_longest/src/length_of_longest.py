# Write your solution here

def length_of_longest(myList):

    curLen = len(myList[0])
    word = myList[0]

    for x in myList:
        if len(x)>curLen:
            word = x
            curLen = len(x)
    return curLen


if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = length_of_longest(my_list)
    print(result)