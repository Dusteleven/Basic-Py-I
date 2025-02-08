# write your solution here

def largest():
    with open("numbers.txt") as new_file:
        largest = 0
        for lines in new_file:
            if int(lines)>largest:
                largest = int(lines)
        return(largest)







if __name__ == "__main__":
    print(largest())