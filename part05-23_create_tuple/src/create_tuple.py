# Write your solution here


def create_tuple(x:int, y: int, z: int):
    dum=[x, y, z]
    tup = ()

    a = min(dum)
    b=max(dum)
    c=sum(dum)

    tup=(a,b,c)
    return tup












if __name__ == "__main__":
    print(create_tuple(5, 3, -1))