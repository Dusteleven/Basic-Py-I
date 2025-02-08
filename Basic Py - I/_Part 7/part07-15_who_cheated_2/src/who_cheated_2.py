# Write your solution here

import csv
from datetime import datetime, timedelta


def final_points():


    students={}
    with open("start_times.csv") as new_file:
        for line in csv.reader(new_file, delimiter=";"):
            student=line[0]
            start_time=datetime.strptime(line[1], "%H:%M")
            
            students[student] = { 
                'start_time': start_time,
                'stats': {
                'task':[],
                'points':[],
                'sub_time':[],
                }
            }

    with open("submissions.csv") as new_file:
        for line in csv.reader(new_file, delimiter=";"):
           student = line[0]
           task = int(line[1])
           points = int(line[2])
           sub_time = datetime.strptime(line[3], "%H:%M")

           students[student]['stats']['task'].append(task)
           students[student]['stats']['points'].append(points)
           students[student]['stats']['sub_time'].append(sub_time) 
  

    Fpoints={}

    for student, info in students.items():
        points_count={}
        start_time = info['start_time']

        tasks = info['stats']['task']
        points = info['stats']['points']
        sub_time = info['stats']['sub_time']


        for i in range(len(tasks)):
            a=(sub_time[i]-start_time)
                
            if int(a.total_seconds()//60)<180:
                if tasks[i] not in points_count:
                    points_count[tasks[i]]=[]
                    points_count[tasks[i]]=(points[i])
                elif tasks[i] in points_count:
                    if points[i]>points_count[tasks[i]]:
                        points_count[tasks[i]]=points[i]
            i+=1
        
        sum_points =0
        for task, points in points_count.items():
            sum_points+=points
        #entry = {student:sum_points}
        Fpoints[student]=sum_points


    return Fpoints       



            
        #for info, data in stats.items():
            #



            #sub_time = info['stats']['sub_time']

        #search tasks 1-8
        #if multiple use highest
        #check time difference >180  mins ignore


#{'matti': 43, 'erkki': 45, 'antti': 41, 'emilia': 42, 'henrik': 37, 'arto': 40, 'esko': 45, 'kjell': 47, 'jyrki': 41, 'teemu': 43, 'tiina': 36, 'jenna': 38, 'virpi': 39, 'kalle': 46, 'maija': 40, 'uolevi': 34, 'anna': 45, 'liisa': 42, 'kotivalo': 43, 'justiina': 44, 'matteus': 30, 'markus': 35, 'luukas': 40, 'johannes': 39}. Now dictionary was {'matti': [43], 'erkki': [45], 'antti': [41], 'emilia': [42], 'henrik': [37], 'arto': [40], 'esko': [45], 'kjell': [47], 'jyrki': [41], 'teemu': [43], 'tiina': [36], 'jenna': [38], 'virpi': [39], 'kalle': [46], 'maija': [40], 'uolevi': [34], 'anna': [45], 'liisa': [42], 'kotivalo': [43], 'justiina': [44], 'matteus': [30], 'markus': [35], 'luukas': [40], 'johannes': [39]} and correct answer is {'matti': 43, 'erkki': 45, 'antti': 41, 'emilia': 42, 'henrik': 37, 'arto': 40, 'esko': 45, 'kjell': 47, 'jyrki': 41, 'teemu': 43, 'tiina': 36, 'jenna': 38, 'virpi': 39, 'kalle': 46, 'maija': 40, 'uolevi': 34, 'anna': 45, 'liisa': 42, 'kotivalo': 43, 'justiina': 44, 'matteus': 30, 'markus': 35, 'luukas': 40, 'johannes': 39}









if __name__ == "__main__":
    #file = "file1.json"
    #print(retrieve_all())
    print(final_points())