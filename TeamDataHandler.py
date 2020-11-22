import csv
import os
from abc import ABC, abstractmethod


class TeamDataHandler(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def read_team_table(self):
        team_dict = {}
        current_folder = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_folder, 'team.csv')
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
            return team_dict
        except:
            pass
        
    @abstractmethod
    def replace_team_table(self, replacement_dict):
        current_folder = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_folder, 'team.csv')
        write_team = open(file_path, 'w', newline='')
        try:  
            writer = csv.writer(write_team, delimiter=';')
            for team_id in replacement_dict.keys():
                writer.writerow([str(team_id), replacement_dict[team_id]['Team Name'], replacement_dict[team_id]['Division'], replacement_dict[team_id]['Sport']])
        except:
            pass
        write_team.close()
