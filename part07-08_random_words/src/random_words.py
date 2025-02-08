# Write your solution here

from random import shuffle

def words(n:int, beginning: str):

    list_of_words=[]
    with open("words.txt") as new_file:
        for line in new_file:
            if line.startswith(beginning):
                list_of_words.append(line.strip())
    

    rNums = list(range(len(list_of_words)))

    if len(rNums)<n:
        raise ValueError("not enough unique words to complete")

    shuffle(rNums)
    output=[]

    for i in range(n):
        y=rNums[i]
        output.append(list_of_words[rNums[i]])

    return output




if __name__ == "__main__":
        result = words(6, "ca")
        
        for i in result:
            print(i)