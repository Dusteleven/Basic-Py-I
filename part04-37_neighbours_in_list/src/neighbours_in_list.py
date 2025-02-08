# Write your solution here


def longest_series_of_neighbours(myList):
    count = 1
    lcount =0
    i=0
    j=1

    while i < len(myList)-1:

        if abs(myList[i] - myList[j])<2:
            count +=1
            if count > lcount:
                lcount = count
        else:
            count = 1
        i+=1
        j+=1
    
    return lcount




if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))





