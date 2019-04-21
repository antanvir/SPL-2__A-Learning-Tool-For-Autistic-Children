import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QMainWindow
from PyQt5.QtWidgets import QLabel, QPushButton
#from JigsawPuzzle import JigsawPuzzle as jp
from LearningModule import LearningModule
#from JigsawPuzzle import JigsawPuzzle
import mysql.connector
from gi.repository import Gdk
class UserDevelopment(QWidget):
    def __init__(self, parent=None):
        super(UserDevelopment, self).__init__(parent)

        self.title = 'LEARNING DEVELOPMENT OF USER'
        self.left = 50
        self.top = 50
        s = Gdk.Screen.get_default()
        print(s.get_width(), s.get_height())
        self.width = s.get_width() # 680
        self.height = s.get_height() # 480
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
        self.picUser.setPixmap(QPixmap("user.png"))
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
        self.lblLearnedObj.setStyleSheet("font-size: 38px; font-weight: bold;")
        self.objList = QLabel()
        self.objList.setStyleSheet("font-size: 25px")
        finalList= list()
        finalList.append(" ")
        finalList.append("0:00:03")
        finalList.append("0:00:02")
        finalList.append("0:00:05")
        finalList.append("0:00:06")
        finalList.append("0:00:08")
        finalList.append("0:00:02")
        finalList.append("0:00:03")
        finalList.append("0:00:03")
        finalList.append("0:00:04")
        finalList.append("0:00:05")
        '''
        listItem = []
        listItem.append('Nothing Learned Yet\n')
        listItem.append('Will Be Upgraded Soon\n')
        '''
        listItem = ""
        listItem += 'Nothing Learned Yet\n'
        listItem += 'Will Be Upgraded Soon\n'
        

        
        mydb = mysql.connector.connect(
            host = 'localhost',
            user = "root",
    #passwd = "",
            database = "spl"
    #auth_plugin='mysql_native_password'
        )
        anika=list()
        i=int(1)
        final=""
        for i in range(1,4):
            myCursor = mydb.cursor()
            sql = "SELECT qid, elapsedTime from questions where qid=%s"
            val=(i,)
            print(i)
            myCursor.execute(sql,val)
            row=myCursor.fetchone()
            
            final+="Object "
            final+=str(row[0])
            final+=" took "
            final+=str(row[1])
            final+=" seconds "
            final+=" while test group took "
            final+=str(finalList[i])
            final+=" seconds\n"
            print(final)
        self.objList.setText(final)
        mydb.commit()
        myCursor.close()
        mydb.close()


        vbox2.addWidget(self.lblLearnedObj)
        vbox2.addWidget(self.objList)

        # Right
        self.lblCorretAns = QLabel()
        self.lblCorretAns.setText(
            "Objects Identified Correctly in Question:\n")
        self.lblCorretAns.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.CorrAnsList = QLabel()
        self.CorrAnsList.setStyleSheet("font-size: 25px")
        '''
        listItem = []
        listItem.append('Nothing Learned Yet\n')
        listItem.append('Will Be Upgraded Soon\n')
        '''
        mydb = mysql.connector.connect(
            host = 'localhost',
            user = "root",
    #passwd = "",
            database = "spl"
    #auth_plugin='mysql_native_password'
        )
        final=""
        for i in range(1,4):
            myCursor = mydb.cursor()
            sql = "SELECT qid, result from questions where qid=%s"
            val=(i,)
            print(i)
            myCursor.execute(sql,val)
            row=myCursor.fetchone()
            
            final+="Object "
            final+=str(row[0])
            final+=" was learned "
            if str(row[1])== "correct":
                final+=" correctly\n"
            else:
                final+=" incorrectly\n"
            print(final)
        self.CorrAnsList.setText(final)
        mydb.commit()
        myCursor.close()
        mydb.close()

        correctItem = ""
        correctItem += 'SPL2 Project\n'
        correctItem += 'Learning Tool For Autistic Children\n'
        

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
