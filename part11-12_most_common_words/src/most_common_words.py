# WRITE YOUR SOLUTION HERE:


import os, string


def most_common_words(filename: str, lower_limit: int):
    all_words = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().translate(str.maketrans('','',string.punctuation)).split()
            all_words.extend(parts)


    final =  {word: all_words.count(word) for word in set(all_words) if all_words.count(word)>= lower_limit}
    
    return final


if __name__ == "__main__":
    
    print("Current working directory:", os.getcwd())
    print (most_common_words("comprehensions.txt", 3))
