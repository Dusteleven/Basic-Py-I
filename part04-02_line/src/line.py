def line(n,s):


    star = "*"*n

    if s =="":
        print (star)
    else:
        print (s[0]*n)



# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")