import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QMainWindow, QPushButton, QLabel
#from JigsawPuzzle import JigsawPuzzle as jp
from LearningModule import LearningModule
from JigsawPuzzle import JigsawPuzzle
from UserDevelopment import UserDevelopment
import tkinter as tk

class StartingPage(QWidget):
    def __init__(self, parent=None):
        super(StartingPage, self).__init__(parent)

        root = tk.Tk()
        self.width = root.winfo_screenwidth()
        self.height = root.winfo_screenheight()
        self.left = 0
        self.top = 0

        self.title = 'WELCOME'
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background-color: rgb(54, 75, 109);")

        self.initUI()

    def initUI(self):

        horUnit = int(self.width / 12)
        verUnit = int(self.height / 12)

        self.label = QLabel(self)
        self.label.setText(" CHOOSE  ANY  MODULE \n___________________________")
        self.label.setGeometry(3*horUnit, 0.5*verUnit, 6*horUnit, 1.5*verUnit)
        self.label.setStyleSheet("color: white; font-size: 35px; font-weight: bold;")
        self.label.setAlignment(Qt.AlignCenter)


        self.btn1 = QPushButton("LEARN  DIFFERENT  OBJECTS", self)
        self.btn1.setGeometry(3*horUnit, 3*verUnit, 6*horUnit, 1*verUnit)
        self.btn1.setStyleSheet("background-color: white; font-weight: bold; font-size: 25px; color: green;")
        self.btn1.clicked.connect(self.btn_1_clicked)


        self.btn2 = QPushButton("PLAY  PUZZLE  GAMES", self)
        self.btn2.setGeometry(3*horUnit, 5.5*verUnit, 6*horUnit, 1*verUnit)
        self.btn2.setStyleSheet("background-color: white; font-weight: bold; font-size: 25px; color: green;")
        self.btn2.clicked.connect(self.btn_2_clicked)


        self.btn3 = QPushButton("SHOW  MY  DEVELOPMENT", self)
        self.btn3.setGeometry(3*horUnit, 8*verUnit, 6*horUnit, 1*verUnit)
        self.btn3.setStyleSheet("background-color: white; font-weight: bold; font-size: 25px; color: green;")
        self.btn3.clicked.connect(self.btn_3_clicked)


    def btn_1_clicked(self):
        self.learn = LearningModule()
        self.learn.show()


    def btn_2_clicked(self):

        self.game = JigsawPuzzle()
        self.game.initGame()
       

    def btn_3_clicked(self):
        self.dev = UserDevelopment()
        self.dev.show()


def main():
    app = QApplication(sys.argv)
    obj = StartingPage()
    obj.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
