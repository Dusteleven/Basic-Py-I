# Write your solution here

from difflib import get_close_matches

if True:
    sent = input("Write text: ")
else:
    sent = 'This is acually a good and usefull program'
input_list = sent.split(" ")


with open("wordlist.txt") as new_file:
    possible_dic={}
    correct_words = []

    for line in new_file:
        correct_words.append(line.strip())

    for input_word in input_list:
        if input_word.lower() in correct_words:
            continue
        else: 
            loc= input_list.index(input_word)
            input_list[loc]=(f"*{input_word}*")
            possible_dic[input_word]=get_close_matches(input_word, correct_words)

for word in input_list:
    print(f"{word} ", end='')
#print("\n")
print("\nsuggestions: ")
for word, sugs in possible_dic.items():
    print(f"{word}: {", ".join(sugs)}")