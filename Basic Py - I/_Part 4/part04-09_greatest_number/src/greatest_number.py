

def greatest_number(a,b,c):
    if a==b==c:
        return a
    elif a!=b and a!=c and b!=c:
        if a>b and a>c:
            return a
        elif b>a and b>c:
            return b
        else: return c
    elif a==b:
        if a>c:
            return a
        elif c>a:
            return c
    elif a==c:
        if a>b:
            return a
        elif b>a:
            return b
    elif b==c:
        if b>a:
            return b
        elif a>b:
            return a








# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(1, 1, 1)
    print(greatest)