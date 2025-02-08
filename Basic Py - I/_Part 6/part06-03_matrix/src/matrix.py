# write your solution here




def matrix_sum():
    with open("matrix.txt") as new_file:
        totalSum=0
        Linesum=0
        for line in new_file:
            lineSum=0
            line=line.replace("\n","")
            parts = line.split(",")
            for a in parts:
                lineSum+=int(a)
            totalSum +=lineSum
        print(totalSum)
    return(totalSum)
        


def matrix_max():
    listMax=0
    totalMax=0
    newparts=[]
    with open("matrix.txt") as new_file:
        for line in new_file:
            line=line.replace("\n","")
            parts = line.split(",")
            for a in parts:
                newparts.append(int(a))


            listMax=max((newparts))
            if listMax>totalMax:
                totalMax=listMax
    print(totalMax)

    return totalMax

def row_sums():
    sumList=[]
    with open("matrix.txt") as new_file:
        for line in new_file:
            sum=0
            line=line.replace("\n","")
            parts = line.split(",")
            for a in parts:
                sum+=int(a)
            sumList.append(sum)
    return sumList







if __name__ == "__main__":
    matrix_sum()
    matrix_max()
    row_sums()
    
