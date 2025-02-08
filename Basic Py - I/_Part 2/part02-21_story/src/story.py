story = " "
last = " "

while True:
        w = input("Please type in a word: ")
        if w=="end" or w==last:
                break
        elif w!="end":
                story += w + " "
                last = w
                
        
                  
print(story)
