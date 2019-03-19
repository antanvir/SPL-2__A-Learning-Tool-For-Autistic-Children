from PyQt5 import QtCore, QtGui, QtWidgets
#-*- coding: utf8 -*-
import mysql.connector
import tkinter as tk
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
import math
from PyQt5 import QtGui, QtCore, QtWidgets, QtMultimedia, QtMultimediaWidgets
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
                             QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget)
from playsound import playsound
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QPixmap, QImage, QImageReader
from PyQt5.QtWidgets import QVBoxLayout
import mysql.connector
from PyQt5.QtMultimedia import QSound
import re

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(774, 604)
        MainWindow.setGeometry(200, 150, 800, 550)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.photo = tk.PhotoImage(file="right.png")
        self.Artwork = tk.Label(self.frame, image=self.photo)
        self.Artwork.photo = self.photo
        self.Artwork.pack()
        

        
    def setDB(self):
        mydb = mysql.connector.connect(
                host = 'localhost',
                user = "root",
                #passwd = "hridita123",
                database = "imageDB"
                #auth_plugin='mysql_native_password'
                )
        myCursor = mydb.cursor(buffered=True)
        sql = "SELECT imagePath1,imagePath2,imagePath3,imagePath4 FROM questions"
        myCursor.execute(sql)
        row=myCursor.fetchall()
        for file in row:
            #print(file)
            ifileName=str(file)
            #print("lol"+ifileName)
            if ifileName:
                self.buttons(ifileName)
    

    def displayAnswer(self, fileName):
        image = Image.open('right.png')
        image.show()
        '''root = tk.Tk()
        label = tk.Label(root)
        label.image = tk.PhotoImage(file='right.png')
        #label['image'] = label.image
        #label.image = immage
        label.pack()
        root.mainloop()'''
        


    def buttons(self,ifileName):
        def change_image():
            response=rb.get()
            mydb = mysql.connector.connect(
                host = 'localhost',
                user = "root",
                #passwd = "hridita123",
                database = "imageDB"
                #auth_plugin='mysql_native_password'
                )
            myCursor = mydb.cursor(buffered=True)
            sql = "SELECT answer FROM questions"
            myCursor.execute(sql)
            row=myCursor.fetchone()
            answer=""
            for file in row:
                #print(file)
                answer=str(file)
            #print(answer)
            if response==answer:
                print("yes")
                w = tk.Label(master, text="Correct Answer", font=("Helvetica", 30))        
                w.pack(side="top")
                img = tk.PhotoImage(file='right.png')
                #label.image = tk.PhotoImage(file='right.png')
                label=tk.Label(master,image=img)
                label.image = img 
                label.pack(side = "bottom")
                sql = "UPDATE questions set result='correct' where qid=1"
                newcur=mydb.cursor()
                newcur.execute(sql)
                mydb.commit()
        
            else:
                print("no")
                w = tk.Label(master, text="Wrong Answer", font=("Helvetica", 30))        
                w.pack()
                img = tk.PhotoImage(file='wrong.png')
                #label.image = tk.PhotoImage(file='right.png')
                label=tk.Label(master,image=img)
                label.image = img 
                label.pack(side = "bottom")
                sql = "UPDATE questions set result='incorrect' where qid=1"
                newcur=mydb.cursor()
                newcur.execute(sql)
                mydb.commit()
            myCursor.close()
            mydb.close()
            
        master = tk.Tk()
        #master.geometry("400x400")
        
        rb= tk.StringVar()
        x = re.split(",|'| ", ifileName)
        print(x[5])
        test="এটা কি?"
        #test = test.decode('utf8')
        print(test)
        #w = tk.Label(master, text=test, font=("Lohit Bengali", 36))        
        #w.pack()
        playsound("tee.wav")
        

        #root = Tk()
        img = tk.PhotoImage(file="qus5.png")
        panel = tk.Label(master, image = img, width=50, height=180)
        panel.image=img
        panel.pack(side = "top", fill = "both", expand = "no")


        option1 = tk.BooleanVar(value=False)

        photo1 = tk.PhotoImage(file=x[1])
        img = Image.open("mango.png")
        width, height = img.size
        photo1=photo1.zoom(3)
        photo1 = photo1.subsample(8)
        r1=tk.Radiobutton(master, image=photo1, variable = rb,value= "mango",command=change_image)
        
        r1.pack(side = "left")
        print(rb.get())

        photo2 = tk.PhotoImage(file=x[5])
        img = Image.open("apple.png")
        width, height = img.size
        photo2=photo2.zoom(1)
        photo2 = photo2.subsample(12)
        r2=tk.Radiobutton(master, image=photo2, value="grape" ,variable = rb,command=change_image)
        r2.pack(side = "right")

        photo3 = tk.PhotoImage(file=x[9])
        img = Image.open("grape.png")
        width, height = img.size

        photo3=photo3.zoom(4)
        photo3 = photo3.subsample(8)
        r3=tk.Radiobutton(master, image=photo3, value= "apple" ,variable = rb,command=change_image)
        r3.pack(side = "left")

        photo4 = tk.PhotoImage(file=x[13])
        img = Image.open("banana.png")
        width, height = img.size

        photo4=photo4.zoom(1)
        photo4 = photo4.subsample(20)
        r4=tk.Radiobutton(master, image=photo4, value="banana",variable = rb,command=change_image)
      
        r4.pack(side = "right")
        master.mainloop()


if __name__ == "__main__":
    import sys
    Ui_MainWindow().setDB()
    '''app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())'''
    #Ui_MainWindow().buttons()'''
    
