from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QBoxLayout
import sys
from tabulate import tabulate
import csv
import os
from abc import ABC, abstractmethod
from hello import helloworld

helloworld()


class Window(QWidget): 

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.showMaximized()

    def init_ui(self):
        layout = QGridLayout()

        # labels



class PlayerDataHandler(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def read_player_table(self):
        player_dict = {}
        current_folder = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_folder, 'player.csv')
        read_player = open(file_path, 'r')
        try:
            for line in read_player:
                row = line.split(';')
                player_dict[row[0]] = {
                    'First Name' : row[1],
                    'Last Name' : row[2],
                    'Password' : row[3],
                    'Email' : row[4],
                    'Jersey Number' : row[5],
                    'Position' : row[6]
                }
            read_player.close()
            return read_player
        except:
            pass

    @abstractmethod
    def replace_player_table(self, replacement_dict):
        current_folder = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_folder, 'player.csv')
        write_player = open(file_path, 'w', newline='')
        try:  
            writer = csv.writer(write_player, delimiter=';')
            for player_id in replacement_dict.keys():
                writer.writerow([str(player_id), replacement_dict[player_id]['First Name'], replacement_dict[player_id]['Last Name'], replacement_dict[player_id]['Password'], replacement_dict[player_id]['Email'], replacement_dict[player_id]['Jersey Number'], replacement_dict[player_id]['Position'], replacement_dict[player_id]['Team']])
        except:
            pass
        write_player.close()

    @abstractmethod
    def add_player(self, first_name, last_name, password, email, jersey_number, position, team):
        working_dict = PlayerDataHandler.read_player_table()
        new_player_id = int(working_dict.keys().max()) + 1
        working_dict[new_player_id] = {
            'First Name' : first_name,
            'Last Name' : last_name,
            'Password' : password,
            'Email' : email,
            'Jersey Number' : jersey_number,
            'Position' : position,
            'Team' : team
        }
        PlayerDataHandler.replace_player_table(working_dict)
        


class TeamDataHandler(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def read_team_table(self):
        team_dict = {}
        current_folder = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_folder, 'player.csv')
        read_team = open(file_path, 'r')
        try:
            for line in read_team:
                row = line.split(';')
                team_dict[row[0]] = {
                    'Team Name' : row[1],
                    'Division' : row[2],
                    'Sport' : row[3],
                }
            read_team.close()
            return read_team
        except:
            pass
        
    @abstractmethod
    def replace_team_table(self, replacement_dict):
        current_folder = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_folder, 'player.csv')
        write_team = open(file_path, 'w', newline='')
        try:  
            writer = csv.writer(write_team, delimiter=';')
            for team_id in replacement_dict.keys():
                writer.writerow([str(team_id), replacement_dict[team_id]['Team Name'], replacement_dict[team_id]['Division'], replacement_dict[team_id]['Sport']])
        except:
            pass
        write_team.close()



class GameDataHandler(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def read_game_table(self):
        game_dict = {}
        current_folder = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_folder, 'player.csv')
        read_game = open(file_path, 'r')
        try:
            for line in read_game:
                row = line.split(';')
                game_dict[row[0]] = {
                    'Date Time' : row[1],
                    'Home Team' : row[2],
                    'Away Team' : row[3],
                }
            read_game.close()
            return read_game
        except:
            pass
        
    @abstractmethod
    def replace_game_table(self, replacement_dict):
        current_folder = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_folder, 'game.csv')
        write_game = open(file_path, 'w', newline='')
        try:  
            writer = csv.writer(write_game, delimiter=';')
            for game_id in replacement_dict.keys():
                writer.writerow([str(game_id), replacement_dict[game_id]['Date Time'], replacement_dict[game_id]['Home Team'], replacement_dict[game_id]['Away Team']])
        except:
            pass
        write_game.close()

