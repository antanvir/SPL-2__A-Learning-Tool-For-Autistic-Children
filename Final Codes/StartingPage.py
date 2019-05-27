import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QMainWindow, QPushButton, QLabel
import tkinter as tk

#from LearningModule import App
#from JigsawPuzzle import JigsawPuzzle
#from UserDevelopment import UserDevelopment
#from new_qus import Ui_MainWindow

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
        self.label.setGeometry(4.5*horUnit, 0.5*verUnit, 6.5*horUnit, 1.5*verUnit)
        self.label.setStyleSheet("color: white; font-size: 35px; font-weight: bold;")
        self.label.setAlignment(Qt.AlignCenter)

        self.btn1 = QPushButton("LEARN  DIFFERENT  OBJECTS", self)
        self.btn1.setGeometry(4.5*horUnit, 3*verUnit, 6.5*horUnit, 1*verUnit)
        self.btn1.setStyleSheet("background-color: white; font-weight: bold; font-size: 25px; color: green;")
        self.btn1.clicked.connect(self.btn_1_clicked)


        self.btn2 = QPushButton("PLAY  PUZZLE  GAMES", self)
        self.btn2.setGeometry(4.5*horUnit, 5*verUnit, 6.5*horUnit, 1*verUnit)
        self.btn2.setStyleSheet("background-color: white; font-weight: bold; font-size: 25px; color: green;")
        self.btn2.clicked.connect(self.btn_2_clicked)


        self.btn3 = QPushButton("EXPRESSIVE  CONTENTS", self)
        self.btn3.setGeometry(4.5*horUnit, 7*verUnit, 6.5*horUnit, 1*verUnit)
        self.btn3.setStyleSheet("background-color: white; font-weight: bold; font-size: 25px; color: green;")
        self.btn3.clicked.connect(self.btn_3_clicked)




        self.label2 = QLabel(self)
        self.label2.setText("CONFIGURATION & PROFILE\n_____________________________")
        self.label2.setGeometry(0.5*horUnit, 0.5*verUnit, 3*horUnit, 1.5*verUnit)
        self.label2.setStyleSheet("color: white; font-size: 23px; font-weight: bold;")
        self.label2.setAlignment(Qt.AlignCenter)
        
        self.btn4 = QPushButton("SHOW  DEVELOPMENT", self)
        self.btn4.setGeometry(0.5*horUnit, 3*verUnit, 3*horUnit, 0.5*verUnit)
        self.btn4.setStyleSheet("background-color: white; font-weight: bold; font-size: 20px; color: black;")
        self.btn4.clicked.connect(self.btn_4_clicked)

        self.btn5 = QPushButton("ADD  MORE  OBJECTS ", self)
        self.btn5.setGeometry(0.5*horUnit, 4.5*verUnit, 3*horUnit, 0.5*verUnit)
        self.btn5.setStyleSheet("background-color: white; font-weight: bold; font-size: 20px; color: black;")
        self.btn5.clicked.connect(self.btn_5_clicked)

        self.btn6 = QPushButton("SET  NEW  QUESTIONS", self)
        self.btn6.setGeometry(0.5*horUnit, 6*verUnit, 3*horUnit, 0.5*verUnit)
        self.btn6.setStyleSheet("background-color: white; font-weight: bold; font-size: 20px; color: black;")
        self.btn6.clicked.connect(self.btn_6_clicked)
        


    def btn_1_clicked(self):
        self.learn = App()
        self.learn.show()


    def btn_2_clicked(self):

        self.game = JigsawPuzzle()
        self.game.initGame(2)
       

    def btn_3_clicked(self):
        self.dev = UserDevelopment()
        self.dev.show()

    def btn_4_clicked(self):
        self.QuesWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        #self.ui.setupUi()
        select=False
        self.ui.setDB(objectID)
        self.QuesWindow.show()


    def btn_4_clicked(self):
        self.dev = UserDevelopment()
        self.dev.show()

    def btn_5_clicked(self):
        self.addObj = UserDevelopment()
        self.addObj.show()

    def btn_6_clicked(self):
        self.addQues = UserDevelopment()
        self.addQues.show()

def main():
    app = QApplication(sys.argv)
    obj = StartingPage()
    obj.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
