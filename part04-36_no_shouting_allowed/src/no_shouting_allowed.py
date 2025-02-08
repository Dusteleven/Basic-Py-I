# Write your solution here


def no_shouting(myList):
    nList = []
    for w in myList:
        if not w.isupper():
            nList.append(w)
    return nList





if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)