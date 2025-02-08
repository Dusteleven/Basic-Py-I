# Write your solution here

def list_sum(aL, bL):
    rL=[]
    i=0
    l=len(aL)
    while i < len(aL):
        rL.append(aL[i]+bL[i])
        i+=1
    return rL

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b))