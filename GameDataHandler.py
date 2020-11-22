


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
