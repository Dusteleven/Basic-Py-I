# Write your solution here
# 
# 
# Please write a function named times_ten(start_index: int, end_index: int), which creates and returns a new dictionary. The keys of the dictionary should be the numbers between start_index and end_index inclusive

#The value mapped to each key should be the key times ten.

#For example:

def times_ten(start_index: int, end_index: int):
    myDic={}
    for i in range(start_index, end_index+1):
        myDic[i]=(i*10)
    return myDic


if __name__ == "__main__":
    d = times_ten(3, 6)
    print(d)