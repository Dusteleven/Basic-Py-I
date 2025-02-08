# tee ratkaisu tänne
# Write your solution here

def get_station_data(filename: str):
    long_lat_dic={}
    with open(filename) as new_file:
        for line in new_file:
            parts=line.split(";")
            if parts[0]=="Longitude":
                continue
            else:
                t = (float(parts[0]), float(parts[1]))
                long_lat_dic[parts[3]]= t
        return long_lat_dic





def distance(stations: dict, station1: str, station2: str):
    import math

    x_km = (stations[station1][0] - stations[station2][0] ) * 55.26
    y_km = (stations[station1][1] - stations[station2][1]) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km

def greatest_distance(stations: dict):
    (longest)=0
    
    for key1, item1 in stations.items():
        for key2, item2 in stations.items():
            if key1!=key2:
                d = distance(stations, key1, key2)
                if d> longest:
                    longest=d
                    Lstation1=key1
                    Lstation2=key2
    longestTuple=(Lstation1, Lstation2, longest)
    return longestTuple







if __name__ == "__main__":

    #stations = get_station_data('stations1.csv')
    #d = distance(stations, "Designmuseo", "Hietalahdentori")
    #print(d)
    #d = distance(stations, "Viiskulma", "Kaivopuisto")
    #print(d)

    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)