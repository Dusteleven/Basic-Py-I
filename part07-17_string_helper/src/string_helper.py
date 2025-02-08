# Write your solution here


import string

def change_case(orig_string: str):
    new_string = orig_string.swapcase()
    return new_string




def split_in_half(orig_str: str):
    length=len(orig_str)
    a=len(orig_str)//2
    b=length-a
    c = orig_str[:a]
    d = orig_str[a:]
    tup = (orig_str[:a],orig_str[a:])

    return(tup)    



def remove_special_characters(orig_string: str):
    new_string=""
    for c in orig_string:
        if c == " " or c in string.ascii_lowercase or c in string.ascii_uppercase or c in string.digits:
            new_string +=c
      
    return new_string



if __name__ == "__main__":

    my_string = "Well hello there!"

    print(change_case(my_string))

    p1, p2 = split_in_half("abcdefg")

    print(p1)
    print(p2)

    m2 = remove_special_characters("This is a test, lets see how it goes!!!11!")
    print(m2)