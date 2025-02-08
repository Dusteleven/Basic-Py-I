# Write your solution here

import json
import os

class HockeyPlayer:
    def __init__(self, name, nationality, assists, goals, penalties, team, games):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games

        

    def __str__(self):
        return (f"{self.name:<21}{self.team:<3} {self.goals:>3} + {self.assists:>2} = {self.goals+self.assists:>3}")



class HockeyPlayerApplication:
    def __init__(self):
        self.__players = [] #list of all player data hockeyplayer objects
        #self.__filehandler=fileHandler()
        
        

    #def load(self, fn):
        #self.__filehandler = fileHandler('partial.json')
        #player_data = self.__filehandler.load_data()
        #self.__players = [HockeyPlayer(**player) for player in player_data]


    def players_in_team(self, team):
        team_list = list(filter(lambda x: x.team == team, self.__players))
        s_list = sorted(team_list, key=lambda x: (x.goals+x.assists), reverse=True)
        for s in s_list:
            print(s)

    def players_from_country(self, country):
        team_list = list(filter(lambda x: x.nationality == country, self.__players))
        s_list = sorted(team_list, key=lambda x: (x.goals + x.assists), reverse=True)
        for s in s_list:
            print(s)

    def help(self):
        print("")
        print("commands: ")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")
    
    #def exit(self):
        #print("execution ended")


    def search(self, name:str):
        match_list = list(filter(lambda p: p.name==name, self.__players))
        if match_list is None:
            print("no matches found")
        else:
            for e in match_list:
                print(e)

    def alpha_teams(self):
        team_list = []
        for p in self.__players:
                team_list.append(p.team)
        set_list = set(team_list)
        f_list = sorted(set_list)

        for team in sorted(f_list):
            print (team)
        
    def alpha_countries(self):
        list_countries = sorted({c.nationality for c in self.__players})
        for d in (list_countries):
            print(d)

    def most_points(self, number):
        sorted_points = sorted(self.__players, key=lambda x: ((x.goals+x.assists), x.goals), reverse=True)

        for i in range(number):
            print (sorted_points[i])

    def most_goals(self, number):
        sorted_points = sorted(self.__players, key = lambda x:(-x.goals, x.games))
        for i in range(number):
            print(sorted_points[i])

    def execute(self):
        
        fn = input("file name: ")
        self.__filehandler = fileHandler(fn)
        player_data = self.__filehandler.load_data()
        self.__players = [HockeyPlayer(**player) for player in player_data]
        print(f"read the data of {len(player_data)} players")



        self.help()
        while True:
            print("")

            try:
                u_input=int(input("command: "))
                if u_input == 0:
                    #self.exit()
                    break
                elif u_input == 1:
                    name = input("name: ")
                    self.search(name)
                elif u_input == 2:
                    self.alpha_teams()
                elif u_input == 3:
                    self.alpha_countries()
                elif u_input == 4:
                    team = input("team: ")
                    self.players_in_team(team)
                elif u_input == 5:
                    country = input("country: ")
                    self.players_from_country(country)

                elif u_input == 6:
                    number = int(input("how many: "))
                    self.most_points(number)

                elif u_input == 7:
                    number = int(input("how many: "))
                    self.most_goals(number)
                else: 
                    print("erroneous input")
                    self.help()
            except ValueError as e:
                print(f"erroneous input")

class fileHandler:
    def __init__(self, filename):
        self.__filename = filename

    def load_data(self):
        with open(self.__filename) as my_file:
            data=my_file.read()
        return json.loads(data)



        
        

#print("Current working directory:", os.getcwd())
application = HockeyPlayerApplication()
application.execute()
    

