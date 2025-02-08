# Write your solution here



def histogram(myString: str):
    myD={}
    for c in myString:
        if c not in myD:
            myD[c]=0
        myD[c] +=1

    for key, value in myD.items():
        print(f"{key} {"*"*value}")









if __name__ == "__main__":
    histogram("abba")