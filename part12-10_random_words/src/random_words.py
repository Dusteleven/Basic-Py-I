# Write your solution here:
import random

def word_generator(characters: str, length: int, amount:int):


    for x in range(amount):
        n_word=''
        r_num = [random.randint(0,len(characters)-1) for i in range(length)]
        for r in r_num:
            n_word += characters[r]
        yield n_word

    




if __name__ == "__main__":
    wordgen = word_generator("abcdefg", 3, 5)
    for word in wordgen:
        print(word)