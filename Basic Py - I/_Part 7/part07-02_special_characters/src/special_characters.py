# Write your solution here

from string import ascii_letters, punctuation

def separate_characters(my_string: str):

    first = ""
    second = ""
    third = ""

    for letter in my_string:
        if letter in ascii_letters:
            first += letter
        elif letter in punctuation:
            second += letter
        else:
            third += letter
    
    return (first, second, third)








if __name__ == "__main__":
    separate_characters("hello !!!** $")