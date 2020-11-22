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


class Window(QWidget): 

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.showMaximized()

    def init_ui(self):
        layout = QGridLayout()


        # labels



