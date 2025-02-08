# Write your solution here


from datetime import time, datetime

import csv

def cheaters():

    start_times=[]
    end_times = []
    start_dic = {}
    end_dic = {}

    with open("start_times.csv") as new_file:
        for line in csv.reader(new_file,delimiter=";"):
            start_times.append(line)
    with open("submissions.csv") as my_file:
        for line in csv.reader(my_file, delimiter=";"):
            end_times.append(line)

    for line in start_times:
        name = line[0]
        time_str = line[1]
        time = datetime.strptime(time_str, '%H:%M').time()
        ftime= datetime.combine(datetime.today(), time)
        start_dic[name]= ftime

    for line in end_times:

        time_str=line[3]
        name = line[0]
        time=datetime.strptime(time_str,'%H:%M').time()
        ftime = datetime.combine(datetime.today(), time)

        if name in end_dic:
            end_dic[name].append(ftime)
        else:
            end_dic[name]=[ftime]

    cheater_list=[]

    for sname, stime in start_dic.items():
                for etime in end_dic[sname]:
                    a=etime-stime
                    mins = int(a.total_seconds()//60)
                    if mins > 180:
                        if sname not in cheater_list:
                            cheater_list.append(sname)
    return cheater_list








if __name__ == "__main__":
    #file = "file1.json"
    #print(retrieve_all())
    print(cheaters())