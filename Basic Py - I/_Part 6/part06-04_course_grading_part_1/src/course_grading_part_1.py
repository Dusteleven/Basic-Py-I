# write your solution here
import os

#cwd = os.getcwd()  # Get the current working directory (cwd)
#files = os.listdir(cwd)  # Get all the files in that directory
#print("Files in %r: %s" % (cwd, files))

if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # hard-coded input
    student_info = 'students1.csv'
    exercise_data = "exercises1.csv"


studD={}
ED={}


with open(student_info) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0]=="id":
            continue
        else:
            studD[parts[0]]= (f"{parts[1].strip()} {parts[2].strip()}")

with open(exercise_data) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0]=="id":
            continue
        else:
            sumDummy=0
            for i in range(1,len(parts)):
                sumDummy+=int(parts[i])
            ED[parts[0]]=sumDummy//10


for id, student in studD.items():
    if id in ED:
        print(f"{student} {ED[id]}")
        

#if __name__ == "__main__"