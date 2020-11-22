import csv
import os
from abc import ABC, abstractmethod


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
        