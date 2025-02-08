# Write your solution here


def add_student(database: dict, name: str):

    if name not in database:
        database[name]="no completed courses"
        return database
    elif name in database:
        return database

def add_course(database: dict, name: str, course_and_grade: tuple):
    newList=[]
    if name in database and course_and_grade[1] !=0:
        if database[name] == "no completed courses":
            newList.append(course_and_grade)
            database[name]=newList

        #name in database, grade not 0
        elif database[name] != "no completed courses":
            thisCourse = course_and_grade[0]
            thisGrade = course_and_grade[1]
     
            listOfCourses=[]
            listOfGrades=[]
            studentData = database[name]   

            foundCourse = False     

            #split values into courses and grades
            for i in range(len(database[name])):
                listOfCourses.append(studentData[i][0])
                listOfGrades.append(studentData[i][1])

            #replace grade ONLY if new grade higher
            if thisCourse in listOfCourses:
                foundCourse = True
                j = listOfCourses.index(thisCourse)
                if thisGrade>listOfGrades[j]:
                    listOfGrades[j]=thisGrade
            elif thisCourse not in listOfCourses:
                foundCourse = False
                listOfCourses.append(thisCourse)
                listOfGrades.append(thisGrade)
            #now list needs to go back into database
    
            for i in range(len(listOfCourses)):
                newList.append((listOfCourses[i], listOfGrades[i]))

            database[name]=newList
    return database

            


def print_student(database: dict, name: str):

    if name in database:   
        #print(name)                         #check if name in database
        courses = database[name]                    #courses should be list of touples

        if courses == "no completed courses":       #if no courses, print none
            print(f"{name}: \n {courses}")
        
        else: 
            print(name+":")                                      #if there are courses iterrate through   
            num_courses = int(len(courses))
            print(f" {num_courses} completed courses:")
            num=0
            sum=0

            for course, grade in courses:
                sum += grade
                num+=1
                print(f"  {course} {grade}")
            print(f" average grade {sum/num}")


        #print(f"{name}: \n  {courses}")
        
    elif name not in database:
        print(f"{name}: no such person in the database")




#mostCourses
#best average (sum grade/num courses)

def summary(database: dict):

    resultList=[]
    nameMostClasses=""
    NumMostClasses=0
    bestAvgGrade=0
    bestAvgGradeName=""
    totalStudents=0
    
    for name in database:
        totalStudents+=1

        courseQ = 0
        gradeSum =0

        for i in range(0,(len(database[name]))):
            courseQ+=1
            gradeSum +=database[name][i][1]
        if courseQ>NumMostClasses:
            NumMostClasses=courseQ
            nameMostClasses=name
        if gradeSum/courseQ>bestAvgGrade:
            bestAvgGrade=gradeSum/courseQ
            bestAvgGradeName=name

    print(f"students {totalStudents}")
    print(f"most courses completed {NumMostClasses} {nameMostClasses}")
    print(f"best average grade {bestAvgGrade:.1f} {bestAvgGradeName}")



    



if __name__ == "__main__":
    students = {}
    add_student(students, "Emily")
    add_student(students, "Peter")
    add_course(students, "Emily", ("Software Development Methods", 4))
    add_course(students, "Emily", ("Software Development Methods", 5))
    add_course(students, "Peter", ("Data Structures and Algorithms", 3))
    add_course(students, "Peter", ("Models of Computation", 0))
    add_course(students, "Peter", ("Data Structures and Algorithms", 2))
    add_course(students, "Peter", ("Introduction to Computer Science", 1))
    add_course(students, "Peter", ("Software Engineering", 3))
    summary(students)
    summary(students)



