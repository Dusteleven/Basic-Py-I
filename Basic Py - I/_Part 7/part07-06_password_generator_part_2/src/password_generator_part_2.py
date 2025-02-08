# Write your solution here

# Write your solution here

import string
from random import shuffle, randint, sample

def generate_strong_password(length: int, nums: bool, special: bool):

    output=[]
    letters = (string.ascii_lowercase)
    numbers = ("0123456789")
    list_special = ("!?=+-()#")
    
    
    while len(output) < (length):

        if len(output) < length:
            output.append(sample(letters,1)[0])
            
        

        if nums:
            if len(output) < length:
                output.append(sample(numbers,1)[0])
            
        
        if special:
            if len(output) < length:
                output.append(sample(list_special,1)[0])
            



    return ("".join(output))

    #final=""
    #final = ("".join(output, len(output)))


    #return final



if __name__ == "__main__":

    # True
    # False
    for i in range(10):
        print(generate_strong_password(2, False, False))