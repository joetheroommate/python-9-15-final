import csv
import os
from abc import ABC, abstractmethod


class PlayerDataHandler(ABC):
    def __init__():
        pass

    @abstractmethod
    def read_player_table():
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
                    'Team' : row[5],
                    'Role' : row[6],
                    'Position' : row[7]
                }
            read_player.close()
            return player_dict
        except:
            pass

    @abstractmethod
    def replace_player_table(replacement_dict):
        current_folder = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_folder, 'player.csv')
        write_player = open(file_path, 'w', newline='')
        try:  
            writer = csv.writer(write_player, delimiter=';')
            for player_id in replacement_dict.keys():
                print(player_id)
                writer.writerow(
                    [
                    str(player_id), replacement_dict[player_id]['First Name'], 
                    replacement_dict[player_id]['Last Name'], 
                    replacement_dict[player_id]['Password'], 
                    replacement_dict[player_id]['Email'], 
                    replacement_dict[player_id]['Team'], 
                    replacement_dict[player_id]['Role'], 
                    replacement_dict[player_id]['Position']
                    ]
                    )
        except:
            pass
        write_player.close()


    # @abstractmethod
    # def update_bank_database(replacement_dict):
    #     current_folder = os.path.dirname(os.path.abspath(__file__))
    #     file_path = os.path.join(current_folder, 'bank.csv')
    #     read_bank_data = open(file_path, 'w', newline='')
    #     try:  
    #         writer = csv.writer(read_bank_data, delimiter=';')
    #         for account in replacement_dict.keys():
    #             writer.writerow([str(account), replacement_dict[account]['First Name'], replacement_dict[account]['Last Name'], replacement_dict[account]['Password'], replacement_dict[account]['Checking Balance'], replacement_dict[account]['Savings Balance']])
    #     except:
    #         pass

    #     read_bank_data.close()

# x = PlayerDataHandler.read_player_table()
# print(x)