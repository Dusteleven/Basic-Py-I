# Write your solution here


def dict_of_numbers():

    

    num0="zero"
    numInt=["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    numTens=["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    numTeens=["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    finalNums=[]
    finalNums.append(num0)
    for i in range(len(numInt)):
        finalNums.append(numInt[i])
    for i in range(len(numTeens)):
        finalNums.append(numTeens[i])
    for i in range(len(numTens)):
        finalNums.append(numTens[i])
        for j in range(len(numInt)):
            finalNums.append(numTens[i]+"-"+numInt[j])
        
    numD={}
    realNums=[]
    for i in range(0,100):
        realNums.append(i)
    
    for i in realNums:
        numD = {realNums[i]:finalNums[i] for i in range(len(realNums))}
    return numD



if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])