# Write your solution here

def most_common_character(myString):
    cnt = 0
    letter = ""

    for c in myString:
        if myString.count(c) > cnt:
            cnt = myString.count(c)
            letter = c
    return letter


if __name__ == "__main__":
    my_list = "aaabb"
    new_list = most_common_character(my_list)
    print(new_list)