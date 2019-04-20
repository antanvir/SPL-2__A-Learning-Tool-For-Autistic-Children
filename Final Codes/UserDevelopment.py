import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QMainWindow
from PyQt5.QtWidgets import QLabel, QPushButton
#from JigsawPuzzle import JigsawPuzzle as jp
from LearningModule import LearningModule
#from JigsawPuzzle import JigsawPuzzle


class UserDevelopment(QWidget):
    def __init__(self, parent=None):
        super(UserDevelopment, self).__init__(parent)

        self.title = 'LEARNING DEVELOPMENT OF USER'
        self.left = 50
        self.top = 50
        self.width = 1250  # 680
        self.height = 620  # 480
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background-color: white;")

        self.initUI()

    def initUI(self):

        layout = QVBoxLayout()
        vbox1 = QVBoxLayout()
        vbox2 = QVBoxLayout()
        vbox3 = QVBoxLayout()
        
        # LEFT
        self.lblDashBoard = QLabel()
        self.lblDashBoard.setText("===  User's Dashboard  ===")
        #self.lblDashBoard = QLabel("===  User's Dashboard  ===")
        self.lblDashBoard.setStyleSheet("font-size: 25px; font-weight: bold;")
        self.lblDashBoard.setAlignment(Qt.AlignCenter)

        self.picUser = QLabel()
        self.picUser.setPixmap(QPixmap("F://Eusha vai//user.png"))
        self.picUser.resize(200, 100)
        self.picUser.move(5, 100)
        vbox1.addWidget(self.picUser)
        #vbox1.addStretch()

        self.lblNameAndPass = QLabel()
        userName = 'First User'
        userPass = 'MyPass123'

        NameText = '\n' + " Username: " + userName + "\n"
        PassText = '\n' + " Password: " + userPass + "\n"

        self.lblNameAndPass.setText(NameText + PassText)
        vbox1.addWidget(self.lblNameAndPass)
        vbox1.addStretch()

        # MIDDLE    
        self.lblLearnedObj = QLabel()
        self.lblLearnedObj.setText("Learned Objects List:\n")
        self.lblLearnedObj.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.objList = QLabel()
        '''
        listItem = []
        listItem.append('Nothing Learned Yet\n')
        listItem.append('Will Be Upgraded Soon\n')
        '''
        listItem = ""
        listItem += 'Nothing Learned Yet\n'
        listItem += 'Will Be Upgraded Soon\n'
        self.objList.setText(listItem)

        vbox2.addWidget(self.lblLearnedObj)
        vbox2.addWidget(self.objList)

        # Right
        self.lblCorretAns = QLabel()
        self.lblCorretAns.setText(
            "Objects Identified Correctly in Question:\n")
        self.lblCorretAns.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.CorrAnsList = QLabel()
        '''
        listItem = []
        listItem.append('Nothing Learned Yet\n')
        listItem.append('Will Be Upgraded Soon\n')
        '''
        correctItem = ""
        correctItem += 'SPL2 Project\n'
        correctItem += 'Learning Tool For Autistic Children\n'
        self.CorrAnsList.setText(correctItem)

        vbox3.addWidget(self.lblCorretAns)
        vbox3.addWidget(self.CorrAnsList)

        hbox = QHBoxLayout()
        hbox.addLayout(vbox1)
        hbox.addStretch()
        hbox.addLayout(vbox2)
        hbox.addStretch()
        hbox.addLayout(vbox3)

        layout.addWidget(self.lblDashBoard)
        #layout.addStretch()
        layout.addLayout(hbox)
        layout.addStretch()
        self.setLayout(layout)
  


def main():
    app = QApplication(sys.argv)
    obj = UserDevelopment()
    obj.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
