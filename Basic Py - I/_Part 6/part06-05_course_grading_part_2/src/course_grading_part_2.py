# wwite your solution here

#cwd = os.getcwd()  # Get the current working directory (cwd)
#files = os.listdir(cwd)  # Get all the files in that directory
#print("Files in %r: %s" % (cwd, files))

if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_points=input("Exam points: ")

else:
    # hard-coded input
    student_info = 'students1.csv'
    exercise_data = "exercises1.csv"
    exam_points="exam_points1.csv"

studD={}
ED={}
examD={}

#get names
with open(student_info) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0]=="id":
            continue
        else:
            studD[parts[0]]= (f"{parts[1].strip()} {parts[2].strip()}")

#get exercise points
with open(exercise_data) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0]=="id":
            continue
        else:
            sumDummy=0
            for i in range(1,len(parts)):
                sumDummy+=int(parts[i].strip())
            ED[parts[0]]=sumDummy
            ED[parts[0]]=sumDummy/40*100//10

with open(exam_points) as new_file:
    for line in new_file:
        parts=line.split(";")
        if parts[0] == ("id"):
            continue
        else:
            sumDummy=0
            for i in range(1, len(parts)):
                sumDummy+=int(parts[i])
            examD[parts[0]]=sumDummy

totalPoints={}

for student in ED:
    if student in examD:
        totalPoints[student]=ED[student]+examD[student]

finalGrade={}

for student in totalPoints:
    if totalPoints[student]<=14:
        finalGrade[student]=0
    elif totalPoints[student]<=17:
        finalGrade[student]=1
    elif totalPoints[student]<=20:
        finalGrade[student]=2
    elif totalPoints[student]<=23:
        finalGrade[student]=3
    elif totalPoints[student]<=27:
        finalGrade[student]=4
    else:
        finalGrade[student]=5

#print
for id, student in studD.items():
    if id in finalGrade:
        print(f"{student} {finalGrade[id]}")