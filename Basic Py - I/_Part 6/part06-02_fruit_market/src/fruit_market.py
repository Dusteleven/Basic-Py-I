# write your solution here

def read_fruits():
    newD={}
    with open("fruits.csv") as new_file:
        for line in new_file:
            line = line.replace("\n",";")
            parts= line.split(";")
            newD[parts[0]]=float(parts[1])
    return(newD)










if __name__ == "__main__":
    print(read_fruits())