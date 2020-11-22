import csv
import os
from abc import ABC, abstractmethod


class GameDataHandler(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def read_game_table(self):
        game_dict = {}
        current_folder = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_folder, 'game.csv')
        read_game = open(file_path, 'r')
        try:
            for line in read_game:
                row = line.split(';')
                game_dict[row[0]] = {
                    'Date' : row[1],
                    'Time' : row[2],
                    'Home Team' : row[3],
                    'Away Team' : row[4],
                }
            read_game.close()
            return game_dict
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

    @abstractmethod
    def add_game(self, first_name, last_name, password, email, jersey_number, position, team):
        working_dict = GameDataHandler.read_game_table()
        new_game_dict = int(working_dict.keys().max()) + 1
        working_dict[new_game_dict] = {
            'Date Time' : first_name,
            'Home Team' : last_name,
            'Away Team' : password,
        }
        GameDataHandler.replace_game_table(working_dict)