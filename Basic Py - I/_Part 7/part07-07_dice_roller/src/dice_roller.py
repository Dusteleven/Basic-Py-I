# Write your solution here

from random import choice

def roll(die: str):

    dieA=[3,3,3,3,3,6]
    dieB=[2,2,2,5,5,5]
    dieC=[1,4,4,4,4,4]
    
    if die == "A":
        
        return choice(dieA)

    elif die == 'B':
        return choice(dieB)

    elif die == 'C':
        return choice(dieC)


def play(die1: str, die2: str, times: int):

    D1 =0
    D2=0
    tie=0

    for i in range(times):

        a = roll(die1)
        b = roll(die2)

        if a>b:
            D1+=1
        elif a<b:
            D2+=1
        elif a==b:
            tie+=1
    
    return(D1,D2,tie)





if __name__ == "__main__":
        result = play("A", "C", 1000)
        print(result)