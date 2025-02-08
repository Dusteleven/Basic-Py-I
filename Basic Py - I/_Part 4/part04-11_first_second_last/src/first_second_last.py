

def first_word(s):
    i=0
    while i < len(s)+1:
        if s[i]==" ":
            return s[:i]
        i+=1

def second_word(s):
    i=0
    space1=0
    space2=0
    while i <= len(s)-1:
        if s[i]==" ":
            if space1==0:
                space1=i+1
                i+=1
                continue
            elif space1!=0:
                space2=i
                return s[space1:space2]
        elif i == len(s)-1:
                space2=i+1
                return s[space1:space2]
        i+=1


def last_word(s):
    i=len(s)-1
    while i>=0:
        if s[i] == " ":
            return s[i+1:]
        i-=1




# You can test your function by calling it within the following block
if __name__ == "__main__":
    #sentence="first second"
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))