# Write your solution here
def distinct_numbers(mL):
    rL=[]
    for a in mL:
        if a not in rL:
            rL.append(a)
    rL=sorted(rL)
    return rL


if __name__ == "__main__":

    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list))