import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget


class StartingPage(QWidget):
    def __init__(self, parent=None):
        super(StartingPage, self).__init__(parent)
        self.title = 'WELCOME'
        self.left = 50
        self.top = 50
        self.width = 1250  # 680
        self.height = 620  # 480
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background-color: rgb(54, 75, 109);")

        self.initUI()

    def initUI(self):
        '''
        space = "       "
        learnTitle = "\n" + space + "Learn Different Objects" + space + "\n"
        gameTitle = "\n" + space + "Play Puzzle Games" + space + "\n"
        developmentTitle = "\n" + space + "Show My Development" + space + "\n"
                '''
        #layout = QVBoxLayout()
        # layout.addStretch()
        self.btn1 = QPushButton("LEARN  DIFFERENT  OBJECTS", self)
        self.btn1.resize(500, 50)
        self.btn1.move(350, 100)
        self.btn1.setStyleSheet("background-color: white; font-weight: bold;")
        self.btn1.clicked.connect(self.btn_1_clicked)
        # layout.addWidget(self.btn1)
        # layout.addStretch()

        self.btn2 = QPushButton("PLAY  PUZZLE  GAMES", self)
        self.btn2.resize(500, 50)
        self.btn2.move(350, 250)
        self.btn2.setStyleSheet("background-color: white; font-weight: bold;")
        # self.b2.setIcon(QIcon(QPixmap("python.gif")))
        self.btn2.clicked.connect(self.btn_2_clicked)
        # layout.addWidget(self.btn2)
        # layout.addStretch()

        self.btn3 = QPushButton("SHOW  MY  DEVELOPMENT", self)
        # self.b3.setEnabled(False)
        self.btn3.resize(500, 50)
        self.btn3.move(350, 400)
        self.btn3.setStyleSheet("background-color: white; font-weight: bold;")
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
        self.show()
        # self.setWindowTitle("WelcomeS")

    def btn_1_clicked(self):
        if self.btn1.isChecked():
            print("button pressed")
        else:
            print("button released")

    def btn_2_clicked(self):
        if self.btn2.isChecked():
            print("button pressed")
        else:
            print("button released")

    def btn_3_clicked(self):
        if self.btn3.isChecked():
            print("button pressed")
        else:
            print("button released")


def main():
    app = QApplication(sys.argv)
    obj = StartingPage()
    #obj.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
