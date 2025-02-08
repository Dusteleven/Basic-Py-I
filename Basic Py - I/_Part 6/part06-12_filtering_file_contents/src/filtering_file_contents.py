# Write your solution here



def split_ogFile():
    parts=[]
    moreparts=[]
    finalparts=[]

    with open("solutions.csv") as new_file:
        for line in new_file:
            parts=(line.split(";"))
            for w in parts:
                if "+" in w:
                    moreparts.append(w.split("+"))
                    moreparts.append("+")
                elif "-" in w:
                    moreparts.append(w.split("-"))
                    moreparts.append("-")
                else: moreparts.append(w.strip())
            finalparts.append(moreparts)
            parts=[]
            moreparts=[]
    return finalparts


def correct(incoming: list):

    with open("correct.csv",'w') as new_file:
        for w in incoming:
            new_file.write(w)


def wrong(incoming: list):

        with open("incorrect.csv",'w') as new_file:
            for w in incoming:
                new_file.write(w)




def filter_solutions():
    answers_matrix=split_ogFile()
    allCorrect=[]
    allWrong=[]
    

    for ans in answers_matrix:
        a=0
        b=0
        c=0
        if ans[2]=="+":
            a=int(ans[1][0])
            b=int(ans[1][1])
            c=int(ans[3])
            if a+b == c:
                allCorrect.append(makeString(ans))
                correct(allCorrect)
            else:
                allWrong.append(makeString(ans))
                wrong(allWrong)
        elif ans[2]=="-":
            a=int(ans[1][0])
            b=int(ans[1][1])
            c=int(ans[3])
            if a-b == c:
                allCorrect.append(makeString(ans))
                correct(allCorrect)
            else:
                allWrong.append(makeString(ans))
                wrong(allWrong)

        
def makeString(ans):
    w=(f"{ans[0]};{ans[1][0]}{ans[2]}{ans[1][1]};{ans[3]}\n")

    return w


if __name__ == "__main__":
    filter_solutions()