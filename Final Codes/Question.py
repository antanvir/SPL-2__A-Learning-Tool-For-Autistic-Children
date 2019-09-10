from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QMainWindow, QPushButton, QLabel
import tkinter as tk
import mysql.connector
import datetime
import pygame

class QuestionWindow(QWidget):
    a=datetime.datetime.now().replace(microsecond=0)
    def __init__(self,object_id,select, parent=None):
        super(QuestionWindow, self).__init__(parent)

        root = tk.Tk()
        self.width = root.winfo_screenwidth()
        self.height = root.winfo_screenheight()
        self.left = 0
        self.top = 0

        self.title = 'Updated Question Panel'
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background-color: white;")

        self.object_id=object_id
        self.select=select
        self.setupUI(self.object_id,self.select)


    def setupUI(self,object_id,select):


        pygame.init()
        horUnit = int(self.width / 12)
        verUnit = int(self.height / 12)

        nameList=list()
        imageList=list()
        qus_nam=""
        audio_nam=""
        #global object_id
        a=datetime.datetime.now().replace(microsecond=0)
        mydb = mysql.connector.connect(
                host = 'localhost',
                user = "root",
                #passwd = "ant904",
                database = "spl"
                #auth_plugin='mysql_native_password'
                )
        myCursor = mydb.cursor(buffered=True)
        sql = "SELECT qus_name,qus_audio,image_name1,image_name2,image_name3,image_name4,imagePath1,imagePath2,imagePath3,imagePath4, answer\
 FROM questions where qid=%s"
        val=(object_id,)
        myCursor.execute(sql,val)
        row=myCursor.fetchone()
        print(row)
        nameList.append(row[2])
        nameList.append(row[3])
        nameList.append(row[4])
        nameList.append(row[5])

        imageList.append(row[6])
        imageList.append(row[7])
        imageList.append(row[8])
        imageList.append(row[9])

        qus_nam=row[0]
        audio_nam=row[1]

        pygame.mixer.music.load(audio_nam) #Loading File Into Mixer
        pygame.mixer.music.play() #Playing It In The Whole Device
        

        self.lblQuestion = QLabel(self)
        self.pixmap = QPixmap(qus_nam)
        self.lblQuestion.setPixmap(self.pixmap)
        self.lblQuestion.setGeometry(3*horUnit, 0*verUnit, 6*horUnit, 3*verUnit)
        self.lblQuestion.setAlignment(QtCore.Qt.AlignCenter)

        self.rButton1 = QtWidgets.QRadioButton(self)
        self.rButton2 = QtWidgets.QRadioButton(self)
        self.rButton3 = QtWidgets.QRadioButton(self)
        self.rButton4 = QtWidgets.QRadioButton(self)

        
        self.rButton1.setIcon(QIcon(imageList[0]))
        self.rButton1.setIconSize(QtCore.QSize(2*horUnit, 2*verUnit))
        self.rButton1.setGeometry(0.5*horUnit, 4*verUnit, 2*horUnit, 2*verUnit)
        self.rButton1.name = nameList[0]
        self.rButton1.toggled.connect(lambda:self.onClicked(object_id,select))


        self.rButton2.setIcon(QIcon(imageList[1]))
        self.rButton2.setIconSize(QtCore.QSize(2*horUnit, 2*verUnit))
        self.rButton2.setGeometry(3.5*horUnit, 4*verUnit, 2*horUnit, 2*verUnit)
        self.rButton2.name = nameList[1]
        self.rButton2.toggled.connect(lambda:self.onClicked(object_id,select))


        self.rButton3.setIcon(QIcon(imageList[2]))
        self.rButton3.setIconSize(QtCore.QSize(2*horUnit, 2*verUnit))
        self.rButton3.setGeometry(6.5*horUnit, 4*verUnit, 2*horUnit, 2*verUnit)
        self.rButton3.name = nameList[2]
        self.rButton3.toggled.connect(lambda:self.onClicked(object_id,select))


        self.rButton4.setIcon(QIcon(imageList[3]))
        self.rButton4.setIconSize(QtCore.QSize(2*horUnit, 2*verUnit))
        self.rButton4.setGeometry(9.5*horUnit, 4*verUnit, 2*horUnit, 2*verUnit)
        self.rButton4.name = nameList[3]
        self.rButton4.toggled.connect(lambda:self.onClicked(object_id,select))

        self.lblResult = QLabel(self)
        # self.pixmap = QPixmap("right.png")
        # self.lblResult.setPixmap(self.pixmap)
        self.lblResult.setGeometry(3*horUnit, 6.8*verUnit, 6*horUnit, 4*verUnit)
        self.lblResult.setAlignment(QtCore.Qt.AlignCenter)
        self.lblResult.setVisible(False)


    def onClicked(self,object_id,select):

        #global select, object_id
        mydb = mysql.connector.connect(
                host = 'localhost',
                user = "root",
                #passwd = "ant904",
                database = "spl"
                #auth_plugin='mysql_native_password'
                )
        myCursor = mydb.cursor(buffered=True)
        sql = "SELECT qus_name,qus_audio,image_name1,image_name2,image_name3,image_name4,imagePath1,imagePath2,imagePath3,imagePath4, answer\
 FROM questions where qid=%s"
        val=(object_id,)
        myCursor.execute(sql,val)
        row=myCursor.fetchone()
        answer=row[10]
        originalAnswer = answer
        buttonPressed = self.sender()

        if buttonPressed.isChecked():
            print(select)
            print("Image pressed is: %s" % (buttonPressed.name))

        if buttonPressed.name == originalAnswer and self.select==False:
            self.select=True
            self.pixmap = QPixmap("right.png")
            self.lblResult.setPixmap(self.pixmap)
            self.lblResult.setVisible(True)
            a=QuestionWindow.a
            b=datetime.datetime.now().replace(microsecond=0)
            c=str(b-a)
            print(b-a)
            pygame.mixer.music.load("/home/anika/Downloads/applause.wav") #Loading File Into Mixer
            pygame.mixer.music.play()
            sql = "update questions set result=%s, elapsedTime=%s where qid=%s"
            val=('correct',c,object_id,)
            #UPDATE products SET ($fields) VALUES ($values) WHERE sku = '$checksku
            newcur=mydb.cursor()
            newcur.execute(sql,val)
            mydb.commit()
        elif buttonPressed.name != originalAnswer and self.select==False:
            self.select=True
            self.pixmap = QPixmap("wrong.png")
            self.lblResult.setPixmap(self.pixmap)
            self.lblResult.setVisible(True)
            a=QuestionWindow.a
            b=datetime.datetime.now().replace(microsecond=0)
            c=str(b-a)
            print(b-a)
            pygame.mixer.music.load("/home/anika/Downloads/failing.mp3") #Loading File Into Mixer
            pygame.mixer.music.play()
            sql = "update questions set result=%s, elapsedTime=%s where qid=%s"
            val=('incorrect',c,object_id)
            newcur=mydb.cursor()
            newcur.execute(sql,val)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    #object_id=int(1)
    #select = False
    
   # display = QuestionWindow(object_id,select)
    display.show()
    sys.exit(app.exec_())