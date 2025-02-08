# Write your solution here

def filter_incorrect():

    #week 2;9,13,14,24,34,35,37
    open('correct_numbers.csv','w').close() #wipe new file name
    correct_file = open("correct_numbers.csv", "a")

    with open("lottery_numbers.csv") as new_file:
        for line in new_file:
            originalLine=line
            line = line.strip()
            largeSplit=line.split(";")
            weekSplit=largeSplit[0].split(" ")
            numList=largeSplit[1].split(",")

            a=checkWeek(weekSplit)
            b=checkNums(numList)

            if a and b:
                with open("correct_numbers.csv", "a") as correct_file:
                    correct_file.write(originalLine)
    correct_file.close()








def checkWeek(weekSplit):
    weeknum=weekSplit[1]
    try:
        weeknum=int(weeknum)
        return True
    except:
        return False


def checkNums(numList):
    try:
       
        if len(numList)!=7:
            return False

        for n in numList:
            num = int(n)
            if  not isinstance(int(num), int):
                return False
            elif not (num>=1 and num<=39):
                return False
            elif numList.count(n)>1:
                return False
        return True
    except: 
        return False
    



if __name__ == "__main__":
    filter_incorrect()
    
