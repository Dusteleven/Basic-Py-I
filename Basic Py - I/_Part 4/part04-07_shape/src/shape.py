def line(n,s):

    star = "*"*n

    if s =="":
        print (star)
    else:
        print (s[0]*n)


def shape(triWidth,triChar, recHeight, recChar):

    i=1
    while i<=triWidth:
        line(i, triChar)
        i+=1


    i=1
    while i<= recHeight:
        line(triWidth, recChar)
        i+=1
    




# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")