def chessboard(a):
    i=1
    white = ("10"*a)
    black = ("01"*a)
    while i<=a:
        if i%2 !=0:
            print(white[:a])
        else:
            print(black[:a])
        i+=1

# Testing the function
if __name__ == "__main__":
    chessboard(3)
