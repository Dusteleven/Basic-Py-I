# Write your solution here

import string
from random import shuffle, randint, sample

def generate_password(length: int):

    output=""
    base_letters = (string.ascii_lowercase)
    #base_letters = list(string.ascii_lowercase)
    
    
    output = "".join(sample(base_letters, length))


    return output



if __name__ == "__main__":
    print(generate_password(2))