# Write your solution here

from random import shuffle, randint

def lottery_numbers(amount: int, lower: int, upper: int):

    baseNums = list(range(lower, upper))
    shuffle(baseNums)
    selectNums = baseNums[0:amount]
    selectNums.sort()

    return selectNums













if __name__ == "__main__":
    lottery_numbers(7,1,40)