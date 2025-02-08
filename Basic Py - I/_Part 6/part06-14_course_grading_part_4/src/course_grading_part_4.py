# tee ratkaisu tänne
if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_points=input("Exam points: ")
    course_info=input("Course information:")

else:
    # hard-coded input
    student_info = 'students1.csv'
    exercise_data = "exercises1.csv"
    exam_points= "exam_points1.csv"
    course_info= "course1.txt"

studD={}
exercise_points_awarded={}
total_exercise_points={}
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
            total_exercise_points[parts[0]]=sumDummy
            exercise_points_awarded[parts[0]]=sumDummy/40*100//10    #EXERCISE POINTS TOTAL

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
course_details=[]

with open(course_info) as new_file:
    for line in new_file:
        parts = line.split(":")
        course_details.append(parts[1].strip())
        

totalPoints={}

for student in exercise_points_awarded:
    if student in examD:
        totalPoints[student]=exercise_points_awarded[student]+examD[student]

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
#studD
#exercise_points_awarded
#total_exercise_points
#examD
#totalPoints
#finalGrade
with open("results.txt", "w") as new_file:
    #add header
    header = (f"{course_details[0]}, {course_details[1]} credits\n")
    new_file.write(header)
    under_line = ((len(header)-1)*"=")
    new_file.write(f"{under_line}\n")
    new_file.write(f"{"name":30}{"exec_nbr":<10}{"exec_pts.":<10}{"exm_pts.":<10}{"tot_pts.":<10}{"grade":<10}\n")
    for id, student in studD.items():
        if id in finalGrade:
            new_file.write(f"{studD[id]:30}{total_exercise_points[id]:<10}{int(exercise_points_awarded[id]):<10}{examD[id]:<10}{int(totalPoints[id]):<10}{finalGrade[id]:<10}\n")

with open("results.csv", "w") as new_file:
    for id, student in studD.items():
        if id in finalGrade:
            new_file.write(f"{id};{studD[id]};{finalGrade[id]}\n")