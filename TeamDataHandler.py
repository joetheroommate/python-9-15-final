import csv
import os
from abc import ABC, abstractmethod


class TeamDataHandler(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def read_team_table():
        team_dict = {}
        current_folder = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_folder, 'team.csv')
        read_team = open(file_path, 'r')
        try:
            for line in read_team:
                row = line.split(';')
                team_dict[row[0]] = {
                    'Captain' : row[1],
                    'Sport' : row[2],
                }
            read_team.close()
            return team_dict
        except:
            pass
        
    @abstractmethod
    def replace_team_table(replacement_dict):
        current_folder = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_folder, 'team.csv')
        write_team = open(file_path, 'w', newline='')
        try:  
            writer = csv.writer(write_team, delimiter=';')
            for team in replacement_dict.keys():
                writer.writerow(
                    [
                    team, 
                    replacement_dict[team]['Captain'], 
                    replacement_dict[team]['Sport'],
                    0
                    ]
                    )
        except:
            pass
        write_team.close()
