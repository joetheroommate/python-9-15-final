import sys
from tabulate import tabulate
import csv
import os
from abc import ABC, abstractmethod
from PlayerDataHandler import PlayerDataHandler
from TeamDataHandler import TeamDataHandler
from GameDataHandler import GameDataHandler


class Interfaces(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def main_menu():
        admin_menu = [
            ["Enter:  ", "For"], 
            ["1", "Create Player Account"], 
            ["2", "Login"], 
            ["3", "Exit"]
            ]

        menu_range = [1, 2, 3]
        menu_choice = input(tabulate(admin_menu))
        try:
            if int(menu_choice) in menu_range:
                pass
            else:
                print("Please choose one of the options")
                Interfaces.main_menu()
        except:
            print("Please choose one of the options")
            Interfaces.main_menu()
            
        if int(menu_choice) == 1:
            Interfaces.player_add()
        elif int(menu_choice) == 2:
            Interfaces.player_login()
        elif int(menu_choice) == 3:
            sys.exit()
        else:
            print("Please choose one of the options")
            Interfaces.main_menu()

    @abstractmethod
    def player_login():
        working_dict = PlayerDataHandler.read_player_table()
        step = 'id'
        while step == 'id':
            active_player_id = input("PLease enter your player ID: ")
            try:
                if active_player_id in working_dict.keys():
                    step = 'pw'
                else:
                    step = 'id'
                    print("Your player ID was not found")
            except:
                print("Your player ID was not found, please try again")
                step = 'id'
                
        while step == 'pw':
            pw = input("Please enter your password: ")
            if pw == working_dict[active_player_id]['Password']:
                step = 'home'
                Interfaces.user_dashboard(active_player_id)
            else:
                step = 'pw'
                print("Your password was incorrect, please try again")

    @abstractmethod
    def user_dashboard(active_player_id):
        working_dict = PlayerDataHandler.read_player_table()
        if working_dict[active_player_id]['Role'] == 'Captain':
            step = 'captain home'
        else:
            step = 'home'
        
        while step == 'home':
            operation = [
                ["Enter:  ", "For"], 
                ["1", "Print My Info"], 
                ["2", "Print Team Info"], 
                ["3", "Print Schedule"], 
                ["4", "Log Out"]
                ]
            menu_range = [1, 2, 3, 4]
            operation_choice = input(tabulate(operation))
            try:
                if int(operation_choice) in menu_range:
                    pass
                else:
                    print("Please choose 1 of the options")
                    Interfaces.main_menu()
            except:
                print("Please choose a of the options")
                step = 'home'
            
            if int(operation_choice) == 1:
                Interfaces.player_print(active_player_id)
            elif int(operation_choice) == 2:
                Interfaces.team_print(active_player_id)
            elif int(operation_choice) == 3:
                Interfaces.game_print(active_player_id)
            elif int(operation_choice) == 4:
                sys.exit()
            step = 'home'


        while step == 'captain home':
            operation = [
                ["Enter:  ", "For"], 
                ["1", "Print My Info"], 
                ["2", "Add Player"], 
                ["3", "Print Team Info"], 
                ["4", "Add Team"], 
                ["5", "Print Schedule"], 
                ["6", "Add Game"], 
                ["7", "Log Out"]
                ]
            menu_range = [1, 2, 3, 4, 5, 6, 7]
            operation_choice = input(tabulate(operation))
            try:
                if int(operation_choice) in menu_range:
                    pass
                else:
                    print("Please choose one of the options")
                    step = 'captain home'
            except:
                print("Please choose 1 of the options")
                step = 'captain home'
                    
            if int(operation_choice) == 1:
                Interfaces.player_print(active_player_id)
            elif int(operation_choice) == 2:
                Interfaces.player_add()
            elif int(operation_choice) == 3:
                Interfaces.team_print(active_player_id)
            elif int(operation_choice) == 4:
                Interfaces.team_add()
            elif int(operation_choice) == 5:
                Interfaces.game_print(active_player_id)
            elif int(operation_choice) == 6:
                Interfaces.game_add()
            elif int(operation_choice) == 7:
                sys.exit()
            step = 'captain home'
                
    @abstractmethod
    def player_print(active_player):
        working_dict = PlayerDataHandler.read_player_table()
        player = [ 
            ["ID: ", active_player], 
            ["Name: ", f"{working_dict[active_player]['First Name']} {working_dict[active_player]['Last Name']}" ], 
            ["Team: ", working_dict[active_player]['Team'] ], 
            ["Role: ", working_dict[active_player]['Role'] ], 
            ["Position: ", working_dict[active_player]['Position'] ] 
            ]
        print(tabulate(player))
        Interfaces.user_dashboard(active_player)

    @abstractmethod
    def team_print(active_player):
        working_team_dict = TeamDataHandler.read_team_table()
        working_player_dict = PlayerDataHandler.read_player_table()
        working_team = working_player_dict[active_player]['Team']
        team = [ 
            ["Team: ", working_team], 
            ["Captain: ", working_team_dict[working_team]['Captain'] ], 
            ["Sport: ", working_team_dict[working_team]['Sport'] ] 
            ]
        print(tabulate(team))
        Interfaces.user_dashboard(active_player)

    @abstractmethod
    def game_print(active_player):
        working_player_dict = PlayerDataHandler.read_player_table()
        working_game_dict = GameDataHandler.read_game_table()
        working_team = working_player_dict[active_player]['Team']
        team_games_list = []

        for game in working_game_dict:
            if working_game_dict[game]['Home Team'] == working_team or working_game_dict[game]['Away Team'] == working_team:
                team_games_list.append(game)

        schedule = [
                    ["Home Team", "Away Team", "Date", "Time"],
                    ['','','','']
                ]

        for game in team_games_list:
            schedule.append([working_game_dict[game]['Home Team'], working_game_dict[game]['Away Team'], working_game_dict[game]['Date'], working_game_dict[game]['Time']])

        print(tabulate(schedule))

    @abstractmethod
    def player_add():
        working_player_dict = PlayerDataHandler.read_player_table()
        keys_list = []
        for id in working_player_dict.keys():
            keys_list.append(int(id))
        keys_list.sort()
        new_player_id = keys_list[-1] + 1
        first_name = input("First name: ")
        last_name = input("Last name: ")
        password = input("Password: ")
        email = input("Email: ")
        team = input("Team: ")
        position = input("Position: ")

        working_player_dict[new_player_id] = {
            'First Name' : first_name,
            'Last Name' : last_name,
            'Password' : password,
            'Email' : email,
            'Team' : team,
            'Role' : 'Player',
            'Position' : position
        }
        PlayerDataHandler.replace_player_table(working_player_dict)
        Interfaces.main_menu()

    @abstractmethod
    def team_add():
        working_team_dict = TeamDataHandler.read_team_table()
        team_name = input("Team Name: ")
        captain = input("Captain Name: ")
        sport = input("Sport: ")

        working_team_dict[team_name] = {
            'Captain' : captain,
            'Sport' : sport
        }
        TeamDataHandler.replace_team_table(working_team_dict)
    
    @abstractmethod
    def game_add():
        print('test 2')
        working_game_dict = GameDataHandler.read_game_table()
        keys_list = []
        for id in working_game_dict.keys():
            keys_list.append(int(id))
        keys_list.sort()
        new_game_id = keys_list[-1] + 1
        game_date = input("Date: ")
        game_time = input("Time: ")
        home_team = input("Home Team: ")
        away_team = input("Away Team: ")

        working_game_dict[new_game_id] = {
            'Date' : game_date,
            'Time' : game_time,
            'Home Team' : home_team,
            'Away Team' : away_team
        }
        GameDataHandler.replace_game_table(working_game_dict)

def main():
    Interfaces.main_menu()
    
if __name__ == '__main__':
    main()