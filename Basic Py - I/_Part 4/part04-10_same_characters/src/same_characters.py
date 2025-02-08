
def same_chars(s,a,b):
    
    if a<0 or b<0 or a>len(s)-1 or b>len(s)-1:
        return False
    elif (s[a]==s[b]):
        return True
    else:
        return False
    


# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))