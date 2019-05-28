import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import mysql.connector
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QMainWindow ,QTableWidget,QTableWidgetItem
from PyQt5.QtWidgets import QLabel, QPushButton, QComboBox, QPlainTextEdit
#from JigsawPuzzle import JigsawPuzzle as jp
from LearningModule import App
#from JigsawPuzzle import JigsawPuzzle
#import mysql.connector
#from gi.repository import Gdk
import tkinter as tk
from graph import MatplotlibWidget, MyWindow
from graphGame import MatplotlibWidget,MyWindowGame
class UserDevelopment(QWidget):
    def __init__(self, parent=None):
        super(UserDevelopment, self).__init__(parent)

        self.title = 'LEARNING DEVELOPMENT OF USER'
        self.left = 0
        self.top = 0
        root = tk.Tk()
        self.width = root.winfo_screenwidth()
        self.height = root.winfo_screenheight()
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
        self.lblDashBoard.setText("\n===  User's Dashboard  ===\n")
        #self.lblDashBoard = QLabel("===  User's Dashboard  ===")
        self.lblDashBoard.setStyleSheet("font-size: 30px; font-weight: bold;")
        self.lblDashBoard.setAlignment(Qt.AlignCenter)

        self.picUser = QLabel()
        self.picUser.setPixmap(QPixmap("user.png"))
        self.picUser.resize(200, 100)
        self.picUser.move(5, 100)
        vbox1.addWidget(self.picUser)
        #vbox1.addStretch()

        self.lblNameAndPass = QLabel()
        self.lblNameAndPass.setStyleSheet("font-weight: normal;")
        userName = 'First User'
        userPass = 'MyPass123'

        NameText = '\n' + " Username:  " + userName + "\n"
        PassText = '\n' + " Password:  " + userPass + "\n"

        self.lblNameAndPass.setText(NameText + PassText)
        vbox1.addWidget(self.lblNameAndPass)
        vbox1.addStretch()

        # MIDDLE    
        self.lblLearnedObj = QLabel()
        self.lblLearnedObj.setText("Object Name       Test Group       Control Group     Correct/Incorrect :\n")
        self.lblLearnedObj.setStyleSheet("font-size: 25px; font-weight: bold;")
        self.objList = QLabel()
        self.objList.setStyleSheet("font-size: 25px")

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(7)
        self.tableWidget.setColumnCount(6)
        
        objectName=list()
        objectName.append(" ")
        objectName.append("Bowl")
        objectName.append("Glass")
        objectName.append("Pillow")
        objectName.append("Pen")
        objectName.append("Mobile")
        objectName.append("Switch")
        objectName.append("Door")
        objectName.append("Bed")
        objectName.append("Water")
        objectName.append("Spoon")
        objectName.append("Pencil")

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
        finalList.append("0:00:12")
        '''
        listItem = []
        listItem.append('Nothing Learned Yet\n')
        listItem.append('Will Be Upgraded Soon\n')
        '''
        listItem = ""
        listItem += 'Nothing Learned Yet\n'
        listItem += 'Will Be Upgraded Soon\n'
        

        self.tableWidget.setShowGrid(False)

        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setColumnWidth(0,250) # 25% Width Column
        self.tableWidget.setColumnWidth(1,250)
        self.tableWidget.setColumnWidth(2,250)
        self.tableWidget.setColumnWidth(3,250)
        self.tableWidget.setColumnWidth(4,250)
        self.tableWidget.setColumnWidth(5,250)
        self.tableWidget.setItem(0,0, QTableWidgetItem("Object no."))
        self.tableWidget.setItem(0,1, QTableWidgetItem("Control group(question time)"))
        self.tableWidget.setItem(0,2, QTableWidgetItem("Test Group(question time)"))
        self.tableWidget.setItem(0,3, QTableWidgetItem("Correct/Incorrect"))
        self.tableWidget.setItem(0,4, QTableWidgetItem("Control Group(Gaming time)"))
        self.tableWidget.setItem(0,5, QTableWidgetItem("Test Group(Gaming time)"))
        mydb = mysql.connector.connect(
            host = 'localhost',
            user = "root",
            #passwd = "ant904",
            database = "spl"
    #auth_plugin='mysql_native_password'
        )
        anika=list()
        i=int(1)
        final=""
        myCursor = mydb.cursor(buffered=True)
        for i in range(1,7):
            sql = "SELECT qid, questions.elapsedTime,game.elapsedTime,result, controlGroup.questionTime,controlGroup.gameTime from questions, game,controlGroup where qid=%s"
            val=(i,)
            print(i)
            myCursor.execute(sql,val)
            row=myCursor.fetchone()
            print(row)
            self.tableWidget.setItem(i,0, QTableWidgetItem(i))
            
            self.tableWidget.setItem(i,1, QTableWidgetItem(row[4]))
            self.tableWidget.setItem(i,2, QTableWidgetItem(row[1]))
            self.tableWidget.setItem(i,3, QTableWidgetItem(row[3]))
            self.tableWidget.setItem(i,4, QTableWidgetItem(row[5]))
            self.tableWidget.setItem(i,5, QTableWidgetItem(row[2]))
            
        
        mydb.commit()
        myCursor.close()
        mydb.close()


        '''vbox2.addWidget(self.lblLearnedObj)
        vbox2.addWidget(self.objList)'''
        
        vbox2.addWidget(self.tableWidget)

        # Right
        
        hbox2=QHBoxLayout()

        #vbx = QVBoxLayout()

        ShowGamingGraph = QPushButton("GAMING Graph")
        ShowGamingGraph.setStyleSheet("background-color: silver;  font-weight: bold;")
        #vbx.addWidget(ShowExpressionData)

        ShowQuestionGraph = QPushButton("QUESTION Graph")
        ShowQuestionGraph.setStyleSheet("background-color: silver;  font-weight: bold;")

        hbox2.addWidget(ShowGamingGraph)
        hbox2.addWidget(ShowQuestionGraph)
        #hbox2.addLayout(vbx)
        
        ShowQuestionGraph.clicked.connect(self.showQus)
        ShowGamingGraph.clicked.connect(self.showGame)

        #ShowExpressionData = QPushButton("EXPRESSION DATA")
        self.ShowExpressionData = QComboBox(self)
        self.ShowExpressionData.addItem("EXPRESSION DATA")
        fileList = list()

        for file in os.listdir("ExpressionOutput"):
            if file.endswith(".txt"):
                fileList.append(file)

        self.ShowExpressionData.addItems(fileList)
        self.ShowExpressionData.setStyleSheet("background-color: silver; font-weight: bold;")


        #ShowExpressionData = QPushButton("EXPRESSION DATA")
        self.ShowEyeGazeData = QComboBox(self)
        self.ShowEyeGazeData.addItem("EYE-GAZE DATA")
        fList = list()

        for file in os.listdir("EyeGazeOutput"):
            if file.endswith(".txt"):
                fList.append(file)

        self.ShowEyeGazeData.addItems(fList)
        self.ShowEyeGazeData.setStyleSheet("background-color: silver; font-weight: bold;")


        self.ShowExpressionData.currentIndexChanged.connect(self.selectionchangeExp)
        self.ShowEyeGazeData.currentIndexChanged.connect(self.selectionchangeEye)

        '''layout = QVBoxLayout()
        layout.addWidget(self.tableWidget) 
        self.setLayout(layout) '''
  
        '''vbox3.addWidget(self.lblCorretAns)
        vbox3.addWidget(self.CorrAnsList)'''

        self.expOutput = QPlainTextEdit(self)
        self.expOutput.setReadOnly(True)
        self.expOutput.setStyleSheet("font-size: 17px; background-color: silver;")
        self.expOutput.insertPlainText("[ Expression output ]:\n_____________________________\n\n")

        self.expOutput1 = QPlainTextEdit(self)
        self.expOutput1.setReadOnly(True)
        self.expOutput1.setStyleSheet("font-size: 17px; background-color: silver;")
        self.expOutput1.insertPlainText("[ Eye-gaze output ]:\n_____________________________\n\n")
        

        hbx = QHBoxLayout()                     #QComboBox
        hbx.addWidget(self.ShowExpressionData)
        hbx.addWidget(self.ShowEyeGazeData)
        
        hbox = QHBoxLayout()    # hbox: Everything without Exp/Eye Output: Upper half
        hbox.addLayout(vbox1)   # vbox1: Left side: profile, buttons, ComboBox
        #hbox.addStretch()
        vbox1.addLayout(hbox2)  # hbox2: Graph plot Button
        vbox1.addStretch()
        vbox1.addLayout(hbx)

        hbox.addLayout(vbox2)   # vbox2: Table part
        
        vbx = QVBoxLayout()         # Main Full Layout
        vbx.addLayout(hbox)

        hbxOutput = QHBoxLayout()           #QPlainText
        hbxOutput.addWidget(self.expOutput)
        hbxOutput.addWidget(self.expOutput1)
        vbx.addLayout(hbxOutput)

        layout.addWidget(self.lblDashBoard)
        #layout.addStretch()
        #layout.addLayout(hbox)
        layout.addLayout(vbx)
        #layout.addStretch()
        self.setLayout(layout)

    def showQus(self):
        self.new_lib = MyWindow()
        self.new_lib.show()
    def showGame(self):
        self.new_lib = MyWindowGame()
        self.new_lib.show()


    def selectionchangeExp(self,i):
        filename = "ExpressionOutput/" + self.ShowExpressionData.currentText()
        file = open(filename, "r")
        contents = file.read()
        print(contents)
        self.expOutput.insertPlainText(contents)

    def selectionchangeEye(self,i):
        filename = "EyeGazeOutput/" + self.ShowExpressionData.currentText()
        file = open(filename, "r")
        contents = file.read()
        print(contents)
        self.expOutput1.insertPlainText(contents)

def main():
    app = QApplication(sys.argv)
    obj = UserDevelopment()
    obj.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
