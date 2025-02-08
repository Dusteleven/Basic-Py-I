# Write your solution here





import urllib.request
import json


def retrieve_all():

    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = my_request.read()
    info = json.loads(data)

    active_list = []
    
    for a in info:
        if a["enabled"] == True:

            fullname = a["fullName"]
            name = a["name"]
            year = a["year"]

            sumE = 0
            for b in a["exercises"]:
                sumE += int(b)

            #dum_tup = ()
            dum_tup = (fullname, name, year, sumE)
            active_list.append(dum_tup)

    return active_list

def retrieve_course(course_name: str):


    master_dic = {}

    my_request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    data = my_request.read()
    info = json.loads(data)

    hours = 0
    students = 0
    hours_average = 0
    exercises = 0
    exercises_average=0

    weeks = len(info)

    for line, data in info.items():
        
        if data["students"]>students:
                students = data["students"]

        h = data["hour_total"]
        hours+=h

        hours_average = hours//students
        
        exercises += data["exercise_total"]

        exercises_average = exercises//students
    
    
    master_dic['weeks'] = weeks
    master_dic['students'] = students
    master_dic['hours'] = hours
    master_dic['hours_average'] = hours_average
    master_dic['exercises'] = exercises
    master_dic['exercises_average'] = exercises_average


    return master_dic








if __name__ == "__main__":
    #file = "file1.json"
    #print(retrieve_all())
    print(retrieve_course("docker2019"))