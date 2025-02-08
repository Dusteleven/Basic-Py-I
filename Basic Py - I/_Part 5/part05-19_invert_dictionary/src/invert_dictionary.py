# Write your solution here


def invert(dictionary: dict):

    newD={}
    for k, v in dictionary.items():
        newD[v]=k
    
    dictionary.clear()

    for k,v in newD.items():
        dictionary[k]=v
    


if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)