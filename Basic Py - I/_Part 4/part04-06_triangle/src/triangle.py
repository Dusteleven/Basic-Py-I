def line(n,s):

    star = "*"*n

    if s =="":
        print (star)
    else:
        print (s[0]*n)


def triangle(size):
    
    i=1
    while i<=size:
        line(i, "#")
        i+=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
