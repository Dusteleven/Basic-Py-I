# Write your solution here

def sum_of_positives(mL):
    sumP = 0
    for c in mL:
        if c>0:
            sumP+=c
    return sumP