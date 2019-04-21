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

        '''
        space = "       "
        learnTitle = "\n" + space + "Learn Different Objects" + space + "\n"
        gameTitle = "\n" + space + "Play Puzzle Games" + space + "\n"
        developmentTitle = "\n" + space + "Show My Development" + space + "\n"
                '''
        self.label = QLabel(self)
        self.label.setText(" CHOOSE  ANY  MODULE \n___________________________")
        self.label.setGeometry(2*horUnit, 0.5*verUnit, 8*horUnit, 1.5*verUnit)
        self.label.setStyleSheet("color: white; font-size: 35px; font-weight: bold;")
        self.label.setAlignment(Qt.AlignCenter)

        #layout = QVBoxLayout()
        # layout.addStretch()
        self.btn1 = QPushButton("LEARN  DIFFERENT  OBJECTS", self)
        #self.btn1.resize(500, 50)
        #self.btn1.move(350, 100)
        self.btn1.setGeometry(2*horUnit, 3*verUnit, 8*horUnit, 1*verUnit)
        self.btn1.setStyleSheet("background-color: white; font-weight: bold; font-size: 25px; color: green;")
        self.btn1.clicked.connect(self.btn_1_clicked)

        # layout.addWidget(self.btn1)
        # layout.addStretch()

        self.btn2 = QPushButton("PLAY  PUZZLE  GAMES", self)
        #self.btn2.resize(500, 50)
        #self.btn2.move(350, 250)
        self.btn2.setGeometry(2*horUnit, 5.5*verUnit, 8*horUnit, 1*verUnit)
        self.btn2.setStyleSheet("background-color: white; font-weight: bold; font-size: 25px; color: green;")
        # self.b2.setIcon(QIcon(QPixmap("python.gif")))
        self.btn2.clicked.connect(self.btn_2_clicked)
        # layout.addWidget(self.btn2)
        # layout.addStretch()

        self.btn3 = QPushButton("SHOW  MY  DEVELOPMENT", self)
        # self.b3.setEnabled(False)
        #self.btn3.resize(500, 50)
        #self.btn3.move(350, 400)
        self.btn3.setGeometry(2*horUnit, 8*verUnit, 8*horUnit, 1*verUnit)
        self.btn3.setStyleSheet("background-color: white; font-weight: bold; font-size: 25px; color: green;")
        self.btn3.clicked.connect(self.btn_3_clicked)
        # layout.addWidget(self.btn3)
        # layout.addStretch()

        '''
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addLayout(layout)
        hbox.addStretch()
		'''
        # self.setLayout(hbox)
        '''
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background-color: lightgray;")
        '''
        # self.show()
        # self.setWindowTitle("WelcomeS")

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
