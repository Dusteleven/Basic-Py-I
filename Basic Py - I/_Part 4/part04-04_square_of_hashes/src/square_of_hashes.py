def line(n,s):


    star = "*"*n

    if s =="":
        print (star)
    else:
        print (s[0]*n)





def square_of_hashes (height):

    i=1
    while i<=height:
        line(height, "#")
        i+=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
