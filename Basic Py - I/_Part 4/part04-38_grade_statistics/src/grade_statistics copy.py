# Write your solution here

def inputNums():
    #numList = [1,2,3,4]
    myList = []
    while True:
        n =(input("Exam points and exercises completed: "))
        if n != "" and n!= " ":
            #trial
            n = n.split(" ")
            for c in n:
                   myList.append(int(c)) #string list
        else: break
    return myList

def exercise_points(mList):
    i = 1
    exP = []
    while i< len(mList):
        if mList[i] < 10:
            exP.append(0 + mList[i-1])
        elif mList[i] <20:
            exP.append(1 + mList[i-1])
        elif mList[i] <30:
            exP.append(2 +mList[i-1])
        elif mList[i] <40:
            exP.append(3 +mList[i-1])
        elif mList[i] <50:
            exP.append(4 +mList[i-1])
        elif mList[i] <60:
            exP.append(5 +mList[i-1])
        elif mList[i] <70:
            exP.append(6 +mList[i-1])
        elif mList[i] <80:
            exP.append(7 +mList[i-1])
        elif mList[i] <90:
            exP.append(8 +mList[i-1])
        elif mList[i] <100:
            exP.append(9 +mList[i-1])
        else:
            exP.append(10 +mList[i-1])
        i+=2
    return exP
          


def grading (exP):
    grades=[]
    for c in exP:
        if c<=14:
            grades.append(0)
        elif c <= 17:
            grades.append(1)
        elif c <= 20:
            grades.append(2)
        elif c <= 23:
            grades.append(3)
        elif c <= 27:
            grades.append(4)
        elif c <= 30:
            grades.append(5)
    return(grades)


def print_out(grades, avPoints):
    
    sum_pass = (i>0 for i in grades)
    pass_perc = (len(grades)-grades.count(0))/len(grades)*100
    

    print("Statistics:")
    print(f"Points average: {avPoints:.1f}")
    print(f"Pass percentage: {pass_perc:.1f}")
    print("Grade distribution: ")

    f = 0

    i = 5
    while i >=0:
        f = grades.count(i)
        print(f"  {i}: " + "*"*f)
        i-=1




def check_fails(mList, exP):
    i=0
    while i<len(mList)-1:
        if mList[i] < 10:
            exP[int(i/2)] = 0
        i+=2
    return exP


def main():
    #mList = [15, 87, 10, 55, 11, 40, 4, 17]
    mList = inputNums()
    exP = exercise_points(mList)
    avPoints = sum(exP)/len(exP)
    corExP = check_fails(mList, exP)
    grades = grading(corExP)
    #grades = [3,1,1,0]
    print_out(grades, avPoints)


main()

