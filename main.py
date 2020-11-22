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
from PlayerDataHandler import PlayerDataHandler
from TeamDataHandler import TeamDataHandler
from GameDataHandler import GameDataHandler


# class Window(QWidget): 

#     def __init__(self):
#         super().__init__()
#         self.init_ui()
#         self.showMaximized()

#     def init_ui(self):
#         layout = QGridLayout()


#         # labels

class Interfaces(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def main_menu():
        admin_menu = [["Enter:  ", "For"], ["1", "Create Player Account"], ["2", "Login"], ["3", "Exit"]]
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
            Interfaces.new_player_input()
        elif int(menu_choice) == 2:
            Interfaces.player_login()
        elif int(menu_choice) == 3:
            pass
        else:
            print("Please choose one of the options")
            Interfaces.main_menu()

    @abstractmethod
    def player_login():
        working_dict = PlayerDataHandler.read_player_table()
        step = 'id'
        while step == 'id':
            player_id = input("PLease enter your player ID: ")
            try:
                if player_id in working_dict.keys():
                    step = 'pw'
                else:
                    step = 'id'
                    print("Your player ID was not found")
            except:
                print("Your player ID was not found, please try again")
                step = 'id'
                
        while step == 'pw':
            pw = input("Please enter your password: ")
            if pw == working_dict[player_id]['Password']:
                step = 'home'
                Interfaces.user_dashboard(player_id)
            else:
                step = 'pw'
                print("Your password was incorrect, please try again")

    @abstractmethod
    def user_dashboard(active_player):
        working_dict = PlayerDataHandler.read_player_table()
        if working_dict['Role'] == 'Captain':
            step = 'captain home'
        else:
            step = 'home'
        
        while step == 'home':
            operation = [["Enter:  ", "For"], ["1", "Print My Info"], ["2", "Print Team Info"], ["3", "Print Schedule"], ["4", "Log Out"]]
            menu_range = [1, 2, 3, 4]
            operation_choice = input(tabulate(operation))
            try:
                if int(operation_choice) == 4:
                    Interfaces.main_menu()
                elif int(operation_choice) in menu_range:
                    step = 'active session'
                else:
                    print("Please choose one of the options")
                    step = 'home'
            except:
                print("Please choose one of the options")
                step = 'home'

        while step == 'captain home':
            operation = [["Enter:  ", "For"], ["1", "Print My Info"], ["2", "Add Player"], ["3", "Print Team Info"], ["4", "Add Team"], ["5", "Print Schedule"], ["6", "Add Game"], ["7", "Log Out"]]
            menu_range = [1, 2, 3, 4, 5, 6, 7]
            operation_choice = input(tabulate(operation))
            try:
                if int(operation_choice) == 7:
                    Interfaces.main_menu()
                elif int(operation_choice) in menu_range:
                    step = 'active session'
                else:
                    print("Please choose one of the options")
                    step = 'home'
            except:
                print("Please choose one of the options")
                step = 'home'


        while step == 'active session':
            account_types = [["Enter:  ", "For"], ["1", "Checking"], ["2", "Savings"]]
            menu_range = [1, 2]
            if operation_choice == 1:
                print("Choose which account to withdraw from: ")
            elif operation_choice == 2:
                print("Choose which account to deposit into: ")
            account_type_choice = input(tabulate(account_types))
            try:
                if int(account_type_choice) in menu_range:
                    pass
                    step = 'amount'
                else:
                    print("PLease choose one of the options")
                    step = 'active session'
            except:
                print("PLease choose one of the options")
                step = 'active session'

        while step == 'amount':
            amount = input("Please enter the amount: ")
            try:
                amount = int(amount)
                step = 'transaction'
            except:
                print("PLease center a valid amount: ")
                step == 'amount'

        while step == 'transaction':
            if int(operation_choice) == 1:
                amount = (int(amount) * -1)
                if int(account_type_choice) == 1:
                    Bank.update_checking(active_player, amount)
                elif int(account_type_choice) == 2:
                    Bank.update_savings(active_player, amount)
            elif int(operation_choice) == 2:
                amount = int(amount)
                if int(account_type_choice) == 1:
                    Bank.update_checking(active_player, amount)
                elif int(account_type_choice) == 2:
                    Bank.update_savings(active_player, amount)



def main():
    Interfaces.main_menu()
    
if __name__ == '__main__':
    main()