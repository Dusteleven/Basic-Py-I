# Write your solution here

def diary_read():
    with open("diary.txt") as new_file:
        parts=[]
        for line in new_file:
            parts.append(line)
    return parts

while True:

    print("1 - add an entry, 2 - read entries, 0 - quit")
    i=int(input("Function: "))


    if (i)==1:
        entry=input("Diary entry: ")
        
        with open("diary.txt",'a') as new_file:
            new_file.write(entry +"\n")
        print("Diary saved")



    elif (i)==2:
        
        parts=diary_read()
        
        print("Entries:")
        if parts:
            for e in parts:
                print((e.strip()))
    
    
    
    elif (i)==0:
        print("Bye now!")
        break




        
