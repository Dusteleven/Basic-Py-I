# Write your solution here

def find_words(search_term: str):

    final_words =[]
    #*************************************************
    if search_term.find("*")!=-1:

        if search_term.find("*")==0:
            new_string=search_term[1:]


            with open("words.txt") as new_file:
                for line in new_file:
                    dummyword = line.strip()
                    if dummyword.endswith(new_string):
                        final_words.append(dummyword)
            


        elif search_term.find("*") == len(search_term)-1:
            new_string=search_term[:(len(search_term)-1)]
            #L = len(search_term)

            with open("words.txt") as new_file:
                for line in new_file:
                    dummyword = line.strip()
                    if  dummyword.startswith(new_string):
                        final_words.append(dummyword)
            #return final_words
    #.................................................
    elif search_term.find(".")!=-1:
        dot_locations=[]
        start=0
        L = len(search_term)

        while search_term.find(".",start)!= -1:
            dot_locations.append(search_term.find(".",start))
            start = search_term.find(".",start)

        with open("words.txt") as new_file:
            for line in new_file:
                dummyword = line.strip()
                if len(line)==L:
                    for i in range(L):
                        if i not in dot_locations:
                            if search_term[i]!=line[i]:
                                break
                                final_words.append(line)
            #return final_words
    else:
        with open("words.txt") as new_file:
            for line in new_file:
                if line == search_term:
                    final_words.append(line)
        #return final_words
    
    return final_words

                            
if __name__ == "__main__":
    print(find_words("art*"))
    #s = "st*"
    #for i in find_words(s):
        #print(i )             
                        
        



            

