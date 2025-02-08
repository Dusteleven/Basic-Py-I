
def balanced_brackets(inc_string: str):

    my_string = ''.join(char for char in inc_string if char in ["(",")","[","]"])

    if len(my_string) == 0:
        return True
    
    if len(my_string) == 1:
        return False
    
    if my_string[0] not in ["(",")","[","]"]:
        return balanced_brackets(my_string[1:])
    
    if my_string[-1] not in ["(",")","[","]"]:
        return balanced_brackets(my_string[:-1])
    
    if (my_string[0] == '('):
        if not my_string[-1] == ')':
            return False
        
    if (my_string[0] == '['):
        if not my_string[-1] == ']':
            return  False
    


    # remove first and last character
    return balanced_brackets(my_string[1:-1])



if __name__ == "__main__":
    ok = balanced_brackets("(x)y)")
    print(ok)