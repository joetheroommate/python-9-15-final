import csv
import os
from abc import ABC, abstractmethod


class GameDataHandler(ABC):
    def __init__():
        pass

    @abstractmethod
    def read_game_table():
        print('test')
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
    def replace_game_table(replacement_dict):
        current_folder = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_folder, 'game.csv')
        write_game = open(file_path, 'w', newline='')
        try:  
            writer = csv.writer(write_game, delimiter=';')
            for game_id in replacement_dict.keys():
                writer.writerow(
                    [
                    str(game_id), 
                    replacement_dict[game_id]['Date'], 
                    replacement_dict[game_id]['Time'],
                    replacement_dict[game_id]['Home Team'], 
                    replacement_dict[game_id]['Away Team'],
                    0
                    ]
                    )
        except:
            pass
        write_game.close()
