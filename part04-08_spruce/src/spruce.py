

def spruce(x):
    print("a spruce!")
    b = " "
    star = "*"
    i=(x-1)
    j=1
    while i>=0:

        print (f"{i*b}{j*star}")


        i-=1
        j+=2
    print (f"{b*(x-1)}*")







# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)